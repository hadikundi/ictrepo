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


if __name__ == "__main__":
    main()
