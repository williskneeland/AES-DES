# GNC - GPU No Coalescing, No Slicing  
Essentially a completely normal parallel AES algorithm. This as standard as parallel AES algorithms get.  
We're storing the sbox and the mul boxes in shared memory as recommended by most parallel AES literature out there. [`aeslib.hpp`](../include/aeslib.hpp) holds the `sbox`, `mul2` and `mul3` that's required for encryption. The three boxes combined use a mere 756 bytes of shared memory, which is more or less trivial for current hardware standards and is completely worth the speed gains.  
The expanded key would also be in shared memory. The input message and the output cipher arrays, however, would continue to be in global memory.  
The main header file with the kernel code and functions is [`parallelcore.cuh`](../include/parallelcore.cuh).

![GNC](../docs/img/gnc.png)