### torch.cuda.memory_stats for vit:
| key | QAT | ViT | QAT - ViT difference|
| ---------------------| --------| -------| ---------------------|
| active.all.allocated | 23497752 | 3735129 | 19762623 |
| active.all.current | 1780 | 721 | 1059 |
| active.all.freed | 23495972 | 3734408 | 19761564 |
| active.all.peak | 2635 | 1300 | 1335 |
| active.large_pool.allocated | 8808954 | 1434171 | 7374783 |
| active.large_pool.current | 333 | 171 | 162 |
| active.large_pool.freed | 8808621 | 1434000 | 7374621 |
| active.large_pool.peak | 890 | 455 | 435 |
| active.small_pool.allocated | 14688798 | 2300958 | 12387840 |
| active.small_pool.current | 1447 | 550 | 897 |
| active.small_pool.freed | 14687351 | 2300408 | 12386943 |
| active.small_pool.peak | 2076 | 922 | 1154 |
| active_bytes.all.allocated | 368.17 TB | 95.31 TB | 272.86 TB |
| active_bytes.all.current | 1.17 GB | 776.49 MB | 420.26 MB |
| active_bytes.all.freed | 368.17 TB | 95.31 TB | 272.86 TB |
| active_bytes.all.peak | 20.72 GB | 19.76 GB | 984.1 MB |
| active_bytes.large_pool.allocated | 367.62 TB | 94.88 TB | 272.74 TB |
| active_bytes.large_pool.current | 1.1 GB | 729.27 MB | 392.77 MB |
| active_bytes.large_pool.freed | 367.62 TB | 94.88 TB | 272.74 TB |
| active_bytes.large_pool.peak | 20.62 GB | 19.67 GB | 977.97 MB |
| active_bytes.small_pool.allocated | 560.36 GB | 440.02 GB | 120.34 GB |
| active_bytes.small_pool.current | 74.72 MB | 47.23 MB | 27.49 MB |
| active_bytes.small_pool.freed | 560.29 GB | 439.97 GB | 120.32 GB |
| active_bytes.small_pool.peak | 102.71 MB | 98.35 MB | 4.35 MB |
| allocated_bytes.all.allocated | 368.17 TB | 95.31 TB | 272.86 TB |
| allocated_bytes.all.current | 1.17 GB | 776.49 MB | 420.26 MB |
| allocated_bytes.all.freed | 368.17 TB | 95.31 TB | 272.86 TB |
| allocated_bytes.all.peak | 20.72 GB | 19.76 GB | 984.1 MB |
| allocated_bytes.large_pool.allocated | 367.62 TB | 94.88 TB | 272.74 TB |
| allocated_bytes.large_pool.current | 1.1 GB | 729.27 MB | 392.77 MB |
| allocated_bytes.large_pool.freed | 367.62 TB | 94.88 TB | 272.74 TB |
| allocated_bytes.large_pool.peak | 20.62 GB | 19.67 GB | 977.97 MB |
| allocated_bytes.small_pool.allocated | 560.36 GB | 440.02 GB | 120.34 GB |
| allocated_bytes.small_pool.current | 74.72 MB | 47.23 MB | 27.49 MB |
| allocated_bytes.small_pool.freed | 560.29 GB | 439.97 GB | 120.32 GB |
| allocated_bytes.small_pool.peak | 102.71 MB | 98.35 MB | 4.35 MB |
| allocation.all.allocated | 23497752 | 3735129 | 19762623 |
| allocation.all.current | 1780 | 721 | 1059 |
| allocation.all.freed | 23495972 | 3734408 | 19761564 |
| allocation.all.peak | 2635 | 1300 | 1335 |
| allocation.large_pool.allocated | 8808954 | 1434171 | 7374783 |
| allocation.large_pool.current | 333 | 171 | 162 |
| allocation.large_pool.freed | 8808621 | 1434000 | 7374621 |
| allocation.large_pool.peak | 890 | 455 | 435 |
| allocation.small_pool.allocated | 14688798 | 2300958 | 12387840 |
| allocation.small_pool.current | 1447 | 550 | 897 |
| allocation.small_pool.freed | 14687351 | 2300408 | 12386943 |
| allocation.small_pool.peak | 2076 | 922 | 1154 |
| inactive_split.all.allocated | 12665290 | 1831976 | 10833314 |
| inactive_split.all.current | 126 | 65 | 61 |
| inactive_split.all.freed | 12665164 | 1831911 | 10833253 |
| inactive_split.all.peak | 168 | 154 | 14 |
| inactive_split.large_pool.allocated | 4576309 | 682776 | 3893533 |
| inactive_split.large_pool.current | 87 | 32 | 55 |
| inactive_split.large_pool.freed | 4576222 | 682744 | 3893478 |
| inactive_split.large_pool.peak | 106 | 116 | -10 |
| inactive_split.small_pool.allocated | 8088981 | 1149200 | 6939781 |
| inactive_split.small_pool.current | 39 | 33 | 6 |
| inactive_split.small_pool.freed | 8088942 | 1149167 | 6939775 |
| inactive_split.small_pool.peak | 90 | 70 | 20 |
| inactive_split_bytes.all.allocated | 316.15 TB | 41.48 TB | 274.68 TB |
| inactive_split_bytes.all.current | 6.05 GB | 635.51 MB | 5.43 GB |
| inactive_split_bytes.all.freed | 316.15 TB | 41.48 TB | 274.67 TB |
| inactive_split_bytes.all.peak | 9.06 GB | 2.68 GB | 6.38 GB |
| inactive_split_bytes.large_pool.allocated | 315.59 TB | 41.04 TB | 274.55 TB |
| inactive_split_bytes.large_pool.current | 6.03 GB | 624.73 MB | 5.42 GB |
| inactive_split_bytes.large_pool.freed | 315.58 TB | 41.04 TB | 274.54 TB |
| inactive_split_bytes.large_pool.peak | 9.04 GB | 2.66 GB | 6.39 GB |
| inactive_split_bytes.small_pool.allocated | 578.21 GB | 446.64 GB | 131.57 GB |
| inactive_split_bytes.small_pool.current | 15.28 MB | 10.77 MB | 4.51 MB |
| inactive_split_bytes.small_pool.freed | 578.2 GB | 446.63 GB | 131.56 GB |
| inactive_split_bytes.small_pool.peak | 25.8 MB | 35.19 MB | -9843712 Bytes |
| max_split_size | -1 | -1 | 0 |
| num_alloc_retries | 0 | 0 | 0 |
| num_ooms | 0 | 0 | 0 |
| oversize_allocations.allocated | 0 | 0 | 0 |
| oversize_allocations.current | 0 | 0 | 0 |
| oversize_allocations.freed | 0 | 0 | 0 |
| oversize_allocations.peak | 0 | 0 | 0 |
| oversize_segments.allocated | 0 | 0 | 0 |
| oversize_segments.current | 0 | 0 | 0 |
| oversize_segments.freed | 0 | 0 | 0 |
| oversize_segments.peak | 0 | 0 | 0 |
| reserved_bytes.all.allocated | 21.16 GB | 20.4 GB | 782.0 MB |
| reserved_bytes.all.current | 20.93 GB | 20.4 GB | 546.0 MB |
| reserved_bytes.all.freed | 236.0 MB | 0 Bytes | 236.0 MB |
| reserved_bytes.all.peak | 20.93 GB | 20.4 GB | 546.0 MB |
| reserved_bytes.large_pool.allocated | 21.05 GB | 20.3 GB | 770.0 MB |
| reserved_bytes.large_pool.current | 20.83 GB | 20.3 GB | 542.0 MB |
| reserved_bytes.large_pool.freed | 228.0 MB | 0 Bytes | 228.0 MB |
| reserved_bytes.large_pool.peak | 20.83 GB | 20.3 GB | 542.0 MB |
| reserved_bytes.small_pool.allocated | 114.0 MB | 102.0 MB | 12.0 MB |
| reserved_bytes.small_pool.current | 106.0 MB | 102.0 MB | 4.0 MB |
| reserved_bytes.small_pool.freed | 8.0 MB | 0 Bytes | 8.0 MB |
| reserved_bytes.small_pool.peak | 106.0 MB | 102.0 MB | 4.0 MB |
| segment.all.allocated | 186 | 224 | -38 |
| segment.all.current | 179 | 224 | -45 |
| segment.all.freed | 7 | 0 | 7 |
| segment.all.peak | 179 | 224 | -45 |
| segment.large_pool.allocated | 129 | 173 | -44 |
| segment.large_pool.current | 126 | 173 | -47 |
| segment.large_pool.freed | 3 | 0 | 3 |
| segment.large_pool.peak | 126 | 173 | -47 |
| segment.small_pool.allocated | 57 | 51 | 6 |
| segment.small_pool.current | 53 | 51 | 2 |
| segment.small_pool.freed | 4 | 0 | 4 |
| segment.small_pool.peak | 53 | 51 | 2 |

# eval() stats
| key | QAT | ViT | QAT - ViT difference|
| ---------------------| --------| -------| ---------------------|
| active.all.allocated | 211295 | 58042 | 153253 |
| active.all.current | 710 | 364 | 346 |
| active.all.freed | 210585 | 57678 | 152907 |
| active.all.peak | 728 | 375 | 353 |
| active.large_pool.allocated | 67202 | 22898 | 44304 |
| active.large_pool.current | 85 | 86 | -1 |
| active.large_pool.freed | 67117 | 22812 | 44305 |
| active.large_pool.peak | 99 | 96 | 3 |
| active.small_pool.allocated | 144093 | 35144 | 108949 |
| active.small_pool.current | 625 | 278 | 347 |
| active.small_pool.freed | 143468 | 34866 | 108602 |
| active.small_pool.peak | 631 | 283 | 348 |
| active_bytes.all.allocated | 24.5 TB | 9.15 TB | 15.34 TB |
| active_bytes.all.current | 590.73 MB | 488.99 MB | 101.73 MB |
| active_bytes.all.freed | 24.49 TB | 9.15 TB | 15.34 TB |
| active_bytes.all.peak | 9.46 GB | 6.09 GB | 3.38 GB |
| active_bytes.large_pool.allocated | 24.49 TB | 9.14 TB | 15.35 TB |
| active_bytes.large_pool.current | 566.94 MB | 465.38 MB | 101.56 MB |
| active_bytes.large_pool.freed | 24.49 TB | 9.14 TB | 15.35 TB |
| active_bytes.large_pool.peak | 9.44 GB | 6.06 GB | 3.38 GB |
| active_bytes.small_pool.allocated | 4.37 GB | 8.4 GB | -4327959552 Bytes |
| active_bytes.small_pool.current | 23.79 MB | 23.62 MB | 175.0 KB |
| active_bytes.small_pool.freed | 4.35 GB | 8.38 GB | -4328138752 Bytes |
| active_bytes.small_pool.peak | 25.8 MB | 25.63 MB | 173.0 KB |
| allocated_bytes.all.allocated | 24.5 TB | 9.15 TB | 15.34 TB |
| allocated_bytes.all.current | 590.73 MB | 488.99 MB | 101.73 MB |
| allocated_bytes.all.freed | 24.49 TB | 9.15 TB | 15.34 TB |
| allocated_bytes.all.peak | 9.46 GB | 6.09 GB | 3.38 GB |
| allocated_bytes.large_pool.allocated | 24.49 TB | 9.14 TB | 15.35 TB |
| allocated_bytes.large_pool.current | 566.94 MB | 465.38 MB | 101.56 MB |
| allocated_bytes.large_pool.freed | 24.49 TB | 9.14 TB | 15.35 TB |
| allocated_bytes.large_pool.peak | 9.44 GB | 6.06 GB | 3.38 GB |
| allocated_bytes.small_pool.allocated | 4.37 GB | 8.4 GB | -4327959552 Bytes |
| allocated_bytes.small_pool.current | 23.79 MB | 23.62 MB | 175.0 KB |
| allocated_bytes.small_pool.freed | 4.35 GB | 8.38 GB | -4328138752 Bytes |
| allocated_bytes.small_pool.peak | 25.8 MB | 25.63 MB | 173.0 KB |
| allocation.all.allocated | 211295 | 58042 | 153253 |
| allocation.all.current | 710 | 364 | 346 |
| allocation.all.freed | 210585 | 57678 | 152907 |
| allocation.all.peak | 728 | 375 | 353 |
| allocation.large_pool.allocated | 67202 | 22898 | 44304 |
| allocation.large_pool.current | 85 | 86 | -1 |
| allocation.large_pool.freed | 67117 | 22812 | 44305 |
| allocation.large_pool.peak | 99 | 96 | 3 |
| allocation.small_pool.allocated | 144093 | 35144 | 108949 |
| allocation.small_pool.current | 625 | 278 | 347 |
| allocation.small_pool.freed | 143468 | 34866 | 108602 |
| allocation.small_pool.peak | 631 | 283 | 348 |
| inactive_split.all.allocated | 94905 | 28516 | 66389 |
| inactive_split.all.current | 22 | 23 | -1 |
| inactive_split.all.freed | 94883 | 28493 | 66390 |
| inactive_split.all.peak | 32 | 30 | 2 |
| inactive_split.large_pool.allocated | 35869 | 10823 | 25046 |
| inactive_split.large_pool.current | 19 | 20 | -1 |
| inactive_split.large_pool.freed | 35850 | 10803 | 25047 |
| inactive_split.large_pool.peak | 27 | 25 | 2 |
| inactive_split.small_pool.allocated | 59036 | 17693 | 41343 |
| inactive_split.small_pool.current | 3 | 3 | 0 |
| inactive_split.small_pool.freed | 59033 | 17690 | 41343 |
| inactive_split.small_pool.peak | 7 | 6 | 1 |
| inactive_split_bytes.all.allocated | 13.71 TB | 4.94 TB | 8.76 TB |
| inactive_split_bytes.all.current | 49.27 MB | 151.01 MB | -106675200 Bytes |
| inactive_split_bytes.all.freed | 13.71 TB | 4.94 TB | 8.76 TB |
| inactive_split_bytes.all.peak | 2.35 GB | 3.06 GB | -770139648 Bytes |
| inactive_split_bytes.large_pool.allocated | 13.7 TB | 4.93 TB | 8.77 TB |
| inactive_split_bytes.large_pool.current | 49.06 MB | 150.62 MB | -106496000 Bytes |
| inactive_split_bytes.large_pool.freed | 13.7 TB | 4.93 TB | 8.77 TB |
| inactive_split_bytes.large_pool.peak | 2.34 GB | 3.06 GB | -771764224 Bytes |
| inactive_split_bytes.small_pool.allocated | 10.33 GB | 12.18 GB | -1981938176 Bytes |
| inactive_split_bytes.small_pool.current | 217.5 KB | 392.5 KB | -179200 Bytes |
| inactive_split_bytes.small_pool.freed | 10.33 GB | 12.18 GB | -1981758976 Bytes |
| inactive_split_bytes.small_pool.peak | 2.09 MB | 2.14 MB | -47104 Bytes |
| max_split_size | -1 | -1 | 0 |
| num_alloc_retries | 0 | 0 | 0 |
| num_ooms | 0 | 0 | 0 |
| oversize_allocations.allocated | 0 | 0 | 0 |
| oversize_allocations.current | 0 | 0 | 0 |
| oversize_allocations.freed | 0 | 0 | 0 |
| oversize_allocations.peak | 0 | 0 | 0 |
| oversize_segments.allocated | 0 | 0 | 0 |
| oversize_segments.current | 0 | 0 | 0 |
| oversize_segments.freed | 0 | 0 | 0 |
| oversize_segments.peak | 0 | 0 | 0 |
| reserved_bytes.all.allocated | 12.73 GB | 8.9 GB | 3.83 GB |
| reserved_bytes.all.current | 12.73 GB | 8.9 GB | 3.83 GB |
| reserved_bytes.all.freed | 0 Bytes | 0 Bytes | 0 Bytes |
| reserved_bytes.all.peak | 12.73 GB | 8.9 GB | 3.83 GB |
| reserved_bytes.large_pool.allocated | 12.7 GB | 8.87 GB | 3.83 GB |
| reserved_bytes.large_pool.current | 12.7 GB | 8.87 GB | 3.83 GB |
| reserved_bytes.large_pool.freed | 0 Bytes | 0 Bytes | 0 Bytes |
| reserved_bytes.large_pool.peak | 12.7 GB | 8.87 GB | 3.83 GB |
| reserved_bytes.small_pool.allocated | 26.0 MB | 26.0 MB | 0 Bytes |
| reserved_bytes.small_pool.current | 26.0 MB | 26.0 MB | 0 Bytes |
| reserved_bytes.small_pool.freed | 0 Bytes | 0 Bytes | 0 Bytes |
| reserved_bytes.small_pool.peak | 26.0 MB | 26.0 MB | 0 Bytes |
| segment.all.allocated | 43 | 40 | 3 |
| segment.all.current | 43 | 40 | 3 |
| segment.all.freed | 0 | 0 | 0 |
| segment.all.peak | 43 | 40 | 3 |
| segment.large_pool.allocated | 30 | 27 | 3 |
| segment.large_pool.current | 30 | 27 | 3 |
| segment.large_pool.freed | 0 | 0 | 0 |
| segment.large_pool.peak | 30 | 27 | 3 |
| segment.small_pool.allocated | 13 | 13 | 0 |
| segment.small_pool.current | 13 | 13 | 0 |
| segment.small_pool.freed | 0 | 0 | 0 |
| segment.small_pool.peak | 13 | 13 | 0 |