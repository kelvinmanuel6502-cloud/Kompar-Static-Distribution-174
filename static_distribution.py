import multiprocessing
import time
import os

def worker_task(task_id, duration):
    start_time = time.time()
    print(f"[PROCESS {os.getpid()}] Menerima Task {task_id} - Beban: {duration}s")
    
    time.sleep(duration)
    
    end_time = time.time()
    print(f"[PROCESS {os.getpid()}] SELESAI Task {task_id} dalam {end_time - start_time:.2f}s")

if __name__ == "__main__":
    tasks_to_assign = [
        (1, 5), # Task 1 beban berat
        (2, 2), # Task 2 beban ringan
        (3, 1), # Task 3 beban sangat ringan
        (4, 4)  # Task 4 beban menengah
    ]
    
    print(f"=== NRP: 174 (GENAP) - STATIC UNEVEN DISTRIBUTION ===")
    print(f"Skenario: Membagi 4 tugas berbeda ke core prosesor secara statis.\n")
    
    processes = []
    total_start = time.time()

    for t_id, dur in tasks_to_assign:
        p = multiprocessing.Process(target=worker_task, args=(t_id, dur))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_end = time.time()
    execution_time = total_end - total_start

    print("-" * 50)
    print(f"TOTAL WAKTU EKSEKUSI: {execution_time:.2f} detik")
    print(f"KESIMPULAN: Distribusi Ideal tercapai karena total waktu")
    print(f"mendekati durasi task terberat (5s), bukan hasil jumlah (12s).")
    print("-" * 50)