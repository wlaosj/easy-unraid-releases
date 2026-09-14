#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Auto Publish Release Assets to Gitee
------------------------------------
This script checks/creates a release on Gitee and uploads all build
artifacts (e.g. Easy-Unraid-Android.apk) to provide a high-speed
mainland China download mirror for users.
"""

import os
import sys
import re
import time
import json
try:
    import requests
except ImportError:
    print("[Gitee Publish] requests library not found, attempting auto install...")
    os.system(f"{sys.executable} -m pip install -q requests")
    import requests

GITEE_API_BASE = "https://gitee.com/api/v5"

def get_env_or_fail(key, default=None):
    val = os.environ.get(key, default)
    if not val:
        print(f"[Gitee Publish] Warning: Environment variable '{key}' is missing or empty.")
    return val

def extract_changelog(version_tag):
    clean_ver = version_tag.lstrip("v")
    changelog = f"🚀 Easy Unraid {version_tag} 发布"
    candidates = ["CHANGELOG.md", "../CHANGELOG.md"]
    for path in candidates:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                pattern = r"##\s*\[" + re.escape(clean_ver) + r"\].*?\n(.*?(?=\n##\s*\[|\Z))"
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    changelog = match.group(1).strip()
                    break
            except Exception as e:
                print(f"[Gitee Publish] Error reading changelog from {path}: {e}")
    return changelog

def ensure_repo_initialized(owner, repo, token):
    headers = {"User-Agent": "Easy-Unraid-CI-Publisher", "Accept": "application/json"}
    check_url = f"{GITEE_API_BASE}/repos/{owner}/{repo}/branches"
    try:
        r = requests.get(check_url, params={"access_token": token}, headers=headers, timeout=15)
        if r.status_code == 200 and isinstance(r.json(), list) and len(r.json()) > 0:
            return True
    except Exception as e:
        print(f"[Gitee Publish] Check branches encountered error: {e}")

    # 若为空仓，自动创建 README.md 产生首个提交与 master 分支
    print(f"[Gitee Publish] Initializing empty repo '{owner}/{repo}' with initial README.md...")
    create_url = f"{GITEE_API_BASE}/repos/{owner}/{repo}/contents/README.md"
    import base64
    content_b64 = base64.b64encode(b"# Easy Unraid (Mainland Mirror)\n\nOfficial Releases mirror.\n").decode("utf-8")
    payload = {
        "access_token": token,
        "content": content_b64,
        "message": "Initial commit for releases mirror"
    }
    try:
        r = requests.post(create_url, json=payload, headers=headers, timeout=15)
        if r.status_code in (200, 201):
            print("[Gitee Publish] Successfully initialized repo with master branch!")
            time.sleep(2)
            return True
    except Exception as e:
        print(f"[Gitee Publish] Auto init repo encountered error: {e}")
    return False

def get_or_create_release(owner, repo, tag_name, token, changelog):
    headers = {
        "User-Agent": "Easy-Unraid-CI-Publisher",
        "Accept": "application/json"
    }

    # 0. 确保仓库非空且具有 master 分支
    ensure_repo_initialized(owner, repo, token)

    # 1. 检查 Release 是否已存在
    check_url = f"{GITEE_API_BASE}/repos/{owner}/{repo}/releases/tags/{tag_name}"
    params = {"access_token": token}
    try:
        r = requests.get(check_url, params=params, headers=headers, timeout=15)
        if r.status_code == 200 and isinstance(r.json(), dict):
            data = r.json()
            print(f"[Gitee Publish] Release '{tag_name}' already exists with ID: {data.get('id')}")
            return data.get("id")
    except Exception as e:
        print(f"[Gitee Publish] Query existing release encountered error: {e}")

    # 2. 如果不存在，则创建新 Release
    create_url = f"{GITEE_API_BASE}/repos/{owner}/{repo}/releases"
    payload = {
        "access_token": token,
        "tag_name": tag_name,
        "name": f"Easy Unraid {tag_name}",
        "body": changelog,
        "prerelease": False,
        "target_commitish": "master"
    }

    print(f"[Gitee Publish] Creating new release '{tag_name}' on Gitee...")
    for attempt in range(1, 4):
        try:
            r = requests.post(create_url, json=payload, headers=headers, timeout=20)
            if r.status_code in (200, 201):
                data = r.json()
                rel_id = data.get("id")
                print(f"[Gitee Publish] Successfully created Release on Gitee! ID: {rel_id}")
                return rel_id
            elif r.status_code == 400 and "已存在" in r.text:
                # 再次查询已有
                r2 = requests.get(check_url, params=params, headers=headers, timeout=15)
                if r2.status_code == 200 and isinstance(r2.json(), dict):
                    return r2.json().get("id")
            print(f"[Gitee Publish] Attempt {attempt} failed: {r.status_code} - {r.text}")
        except Exception as e:
            print(f"[Gitee Publish] Attempt {attempt} failed with exception: {e}")
        time.sleep(2)

    return None

def upload_asset(owner, repo, release_id, token, file_path):
    filename = os.path.basename(file_path)
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    print(f"\n[Gitee Publish] Uploading '{filename}' ({file_size_mb:.2f} MB)...")

    upload_url = f"{GITEE_API_BASE}/repos/{owner}/{repo}/releases/{release_id}/attach_files"
    data = {"access_token": token}

    if file_size_mb > 98.0:
        print(f"[Gitee Publish] ⚠️ Warning: '{filename}' ({file_size_mb:.2f} MB) exceeds Gitee 100MB limit, skipping.")
        return False

    for attempt in range(1, 4):
        try:
            with open(file_path, "rb") as f:
                files = {"file": (filename, f)}
                r = requests.post(upload_url, data=data, files=files, timeout=120)
            
            if r.status_code in (200, 201):
                res_data = r.json()
                dl_url = res_data.get("browser_download_url") or "Uploaded"
                print(f"[Gitee Publish]  '{filename}' uploaded successfully!")
                print(f"                 Download URL: {dl_url}")
                return True
            else:
                print(f"[Gitee Publish] Attempt {attempt} upload failed: {r.status_code} - {r.text}")
        except Exception as e:
            print(f"[Gitee Publish] Attempt {attempt} upload exception: {e}")
        time.sleep(3)

    print(f"[Gitee Publish] ⚠️ Failed to upload '{filename}' after multiple attempts.")
    return False

def main():
    token = os.environ.get("GITEE_TOKEN", "").strip()
    owner = os.environ.get("GITEE_OWNER", "wdv880518").strip()
    repo = os.environ.get("GITEE_REPO", "easy-unraid").strip()
    tag_name = os.environ.get("TAG_NAME", "").strip()
    artifacts_dir = os.environ.get("ARTIFACTS_DIR", "artifacts").strip()

    if not token:
        print("[Gitee Publish] No GITEE_TOKEN found. Skipping Gitee publish.")
        return 0

    if not tag_name:
        print("[Gitee Publish] Error: TAG_NAME is missing.")
        return 0

    print("=" * 60)
    print(f"[Gitee Publish] Target: https://gitee.com/{owner}/{repo}")
    print(f"[Gitee Publish] Tag:    {tag_name}")
    print("=" * 60)

    changelog = extract_changelog(tag_name)
    release_id = get_or_create_release(owner, repo, tag_name, token, changelog)
    if not release_id:
        print("[Gitee Publish] ⚠️ Could not get or create Gitee Release. Skipping assets upload.")
        return 0

    if not os.path.isdir(artifacts_dir):
        print(f"[Gitee Publish] Warning: Artifacts directory '{artifacts_dir}' not found.")
        return 0

    files_to_upload = []
    for f in os.listdir(artifacts_dir):
        p = os.path.join(artifacts_dir, f)
        if os.path.isfile(p) and not f.startswith("."):
            # 优先筛选分发安装包
            if f.endswith((".apk", ".dmg", ".zip", ".exe", ".ipa")):
                files_to_upload.append(p)

    if not files_to_upload:
        print("[Gitee Publish] No binary release assets found in artifacts directory.")
        return 0

    print(f"[Gitee Publish] Found {len(files_to_upload)} assets to upload.")
    success_count = 0
    for p in files_to_upload:
        if upload_asset(owner, repo, release_id, token, p):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"[Gitee Publish] Completed! {success_count}/{len(files_to_upload)} files published to Gitee Release.")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())
