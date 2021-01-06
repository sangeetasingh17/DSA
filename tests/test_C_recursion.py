import sys
sys.path.append('../')

from C_recursion import (
    A_factorial,
    B_fibonnaci,
    C_print_n_to_1,
    D_print_1_to_n,
    E_tail_recursion,
    F_checking_palindrome,
    G_sum_of_digits,
    H_rod_cutting,
    I_subset_of_set,
    J_tower_of_hanoi,
)


class Test_C_recursion:

    def test_A_factorial(self):
        assert A_factorial.method1(0) == 1
        assert A_factorial.method1(1) == 1
        assert A_factorial.method1(2) == 2
        assert A_factorial.method1(4) != 23
        assert A_factorial.method1(10) == 3628800