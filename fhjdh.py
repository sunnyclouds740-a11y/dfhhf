total_modified = sum('✅' in entry for entry in log_entries)
    summary = f"🔧 Tổng số file đã sửa: {total_modified}"
    print(summary)
    log_entries.append(summary)
