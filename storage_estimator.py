# Storage Estimator
# Estimates how much storage a set of files needs.

def estimate_storage(num_files, avg_size_mb):
    """Return the total storage needed in megabytes."""
    return num_files * avg_size_mb


def main():
    print("Storage Estimator")
    num_files = int(input("Enter number of files: "))
    avg_size_mb = float(input("Average size per file is (MB): "))

    total_mb = estimate_storage(num_files, avg_size_mb)
    print("Total:", total_mb, "MB")
    print("In GB:", round(total_mb / 1024,2), "GB")


if __name__ == "__main__":
    main()
