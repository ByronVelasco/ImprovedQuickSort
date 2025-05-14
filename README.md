# Experimental Analysis of Quicksort Algorithm Variants

This project presents a comparative analysis of different versions of the **Quicksort** algorithm through an experimental approach. The purpose is to study and contrast the performance of each variant in terms of execution efficiency, highlighting their theoretical and practical differences.

## Summary

The Quicksort algorithm is one of the most well-known sorting methods due to its average efficiency of **O(n lg n)**. However, its performance can vary significantly depending on the partitioning strategy and other factors. In this project, the following variants are implemented and analyzed:

- Classic Quicksort  
- Randomized Quicksort  
- Quicksort with tail recursion elimination (tre quicksort)
- Quicksort using the median of three random elements as pivot  
- Stooge Sort (included as an extreme reference for its inefficiency)

Each algorithm includes a brief theoretical introduction, and its execution time is measured on random, ascending, and descending sorted lists to objectively compare their behavior.

## Objectives

- Implement various Quicksort algorithm variants.  
- Understand the theoretical differences between each version.  
- Measure and compare execution times of each algorithm across different input scenarios.  
- Identify which Quicksort variant performs best in practice.  
- Contrast these results with an inefficient reference algorithm (Stooge Sort) to highlight the importance of a good partitioning strategy.

## Conclusions

- **Stooge Sort** was, as expected, the least efficient in all scenarios, confirming its didactic purpose and inefficient complexity.  
- For **random lists**, the **classic Quicksort** was the fastest due to its simplicity and lower overhead from additional conditions.  
- For **ascending and descending ordered lists** (edge cases where classic Quicksort tends to degrade), the **randomized**, **tre quicksort**, and **median-of-three** variants delivered better performance by avoiding the worst-case behavior of the classic version.  
- These results demonstrate that the choice of Quicksort variant should consider the expected input type: the classic version is highly efficient on random data, but more robust variants are preferable when the input may have pre-existing order.

## **Project Structure**

The repository is organized into the following components:

- **`1 Stooge Sort` Folder**:  
  This folder contains the implementation of the `stooge_sort` algorithm and its performance comparison with the `bubble_sort` algorithm. It includes an experiment measuring and analyzing their execution times.

- **`2 Improved Versions` Folder**:  
  This folder contains the implementation of algorithms `quick_sort`, `random_quicksort`, `tree_random_quicksort` and `median_quick_sort` and their performance comparison with each other. It includes an experiment measuring and analyzing their execution times.

- **`img/` Folder**:  
  Stores the output images generated during experimentation.  

- **`project_functions.py` Python Script**:  
  This Python script includes all the sorting algorithms developed specifically for this project.

## **Final Note**

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

## **Reference**

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

> Byron Velasco, 2025.  
> *Sorting Algorithms* (GitHub Repository).  
> Available at: [https://github.com/ByronVelasco/SortingAlgorithms](https://github.com/ByronVelasco/SortingAlgorithms)

## **License**

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

© 2025 Byron Velasco