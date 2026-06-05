<!-- Slide number: 1 -->
# Introduction to Computer Architecture
Lecture 01
Instructor: Ayesha Siddika
ASST Professor, SWE, DIU.

<!-- Slide number: 2 -->
# Reference Books
Computer Organization and Architecture: Designing for Performance- William Stallings (8th Edition)
Any later edition is fine

<!-- Slide number: 3 -->
What Is Computer Architecture?
Computer Architecture  =
Instruction Set Architecture + Machine Organization

<!-- Slide number: 4 -->
Instruction Set Architecture
ISA = attributes of the computing system as seen by the programmer
Organization of programmable storage
Data types & data structures
Instruction set
Instruction formats
Modes of addressing
Exception handling

<!-- Slide number: 5 -->
Machine Organization
Capabilities & performance characteristics of principal functional units (e.g., registers, ALU, shifters, logic units)
Ways in which these components are interconnected
Information flow between components
Logic and means by which such information flow is controlled

<!-- Slide number: 6 -->
# Definitions
Computer architecture refers to those attributes of a system visible to a programmer or
Those attributes that have a direct impact on the logical execution of a program
Examples of architectural attributes: Instruction set, the number of bits used to represent various data types (e.g., numbers, characters), I/O mechanisms, and techniques for addressing memory

<!-- Slide number: 7 -->
# Definitions
For example, it is an architectural design issue whether a computer will have a multiply instruction
On the other hand, it is an organizational issue whether that instruction will be implemented by a special multiply unit or by a mechanism that makes repeated use of the add unit of the system

<!-- Slide number: 8 -->
# STRUCTURE AND FUNCTION
A computer is a complex system
The hierarchical nature of complex systems is essential to both their design and their description
The designer need only deal with a particular level of the system at a time
At each level, the system consists of a set of components and their interrelationships and the designer is concerned with associated structure and function:
Structure: The way in which the components are interrelated
Function: The operation of each individual component as part of the structure

<!-- Slide number: 9 -->
# Functional View of a Computer

![](Picture2.jpg)

<!-- Slide number: 10 -->
# Functional units
In general terms, there are only four functional units:
Data processing: The computer must be able to process data
The data may take a wide variety of forms, and the range of processing requirements is broad
Data storage: It is also essential that a computer store data
If the computer is processing data on the fly (i.e., data come in and get processed, and the results go out immediately), the computer must temporarily store at least those pieces of data that are being worked on at any given moment
Thus, there is at least a short-term data storage function
Equally important, the computer performs a long-term data storage function also
Files of data are stored on the computer for subsequent retrieval and update

<!-- Slide number: 11 -->
# Functional units
Data movement: The computer must be able to move data between itself and the outside world
The computer’s operating environment consists of devices that serve as either sources or destinations of data
When data are received from or delivered to a device that is directly connected to the computer, the process is known as input–output(I/O), and the device is referred to as a peripheral
When data are moved over longer distances, to or from a remote device, the process is known as data communications
Control: There must be control of these three functions
This control is exercised by the individual(s) who provides the computer with instructions
Within the computer, a control unit manages the computer’s resources and orchestrates the performance of its functional parts in response to those instructions

<!-- Slide number: 12 -->
# Possible Operations

![](Picture2.jpg)

![](Picture4.jpg)
The computer can function as a data movement device (Figure 1), simply transferring data from one peripheral or communications line to another
It can also function as a data storage device (Figure 2), with data transferred from the external environment to computer storage (read) and vice versa (write)

<!-- Slide number: 13 -->
# Possible Operations

![](Picture4.jpg)

![](Picture3.jpg)
The final two diagrams show operations involving data processing, on data either in storage (Figure 3) or en route between storage and the external environment (Figure 4)

<!-- Slide number: 14 -->
# Structural Units/Components

![](Picture2.jpg)
This is the simplest possible depiction of a computer
The computer interacts in some fashion with its external environment
In general, all of its linkages to the external environment can be classified as peripheral devices or communication lines

<!-- Slide number: 15 -->
# Structural Units/Components
There are four main structural components:
Central processing unit (CPU): Controls the operation of the computer and performs its data processing functions
Often simply referred to as processor
Main memory: Stores data
I/O: Moves data between the computer and its external environment
System interconnection: Some mechanism that provides for communication among CPU, main memory, and I/O
A common example of system interconnection is by means of a system bus, consisting of a number of conducting wires to which all the other components attach

<!-- Slide number: 16 -->
# Top-Level Structure

![](Picture2.jpg)

<!-- Slide number: 17 -->
# Evolution of Computers
First Generation: Vacuum Tubes
The ENIAC (Electronic Numerical Integrator And Computer)
Designed and constructed at the University of Pennsylvania
World’s first general purpose electronic digital computer
Second Generation: Transistors
The first major change in the electronic computer came with the replacement of the vacuum tube by the transistor
The transistor was invented at Bell Labs in 1947
The transistor is smaller, cheaper, and dissipates less heat than a vacuum tube but can be used in the same way as a vacuum tube to construct computers
Unlike the vacuum tube, which requires wires, metal plates, a glass capsule, and a vacuum, the transistor is a solid-state device, made from silicon

<!-- Slide number: 18 -->
# Evolution of Computers
Third Generation and forth: Integrated Circuits
 A single, self-contained transistor is called a discrete component
Throughout the 1950s and early 1960s, electronic equipment was composed largely of discrete components—transistors, resistors, capacitors, and so on
Discrete components were manufactured separately, packaged in their own containers, and soldered or wired together onto masonite-like circuit boards, which were then installed in computers, oscilloscopes, and other electronic equipment
Whenever an electronic device called for a transistor, a little tube of metal containing a pinhead-sized piece of silicon had to be soldered to a circuit board
The entire manufacturing process, from transistor to circuit board, was expensive and cumbersome
In 1958 came the achievement that revolutionized electronics and started the era of microelectronics: the invention of the integrated circuit

<!-- Slide number: 19 -->
# Evolution of Computers
Microelectronics means, literally, “small electronics”
The basic elements of a digital computer: only two fundamental types of components are required
Gates and memory cells
A gate is a device that implements a simple Boolean or logical function, such as IF A AND B ARE TRUE THEN C IS TRUE (AND gate)
Such devices are called gates because they control data flow in much the same way that canal gates do
The memory cell is a device that can store one bit of data; that is, the device can be in one of two stable states at any time
By interconnecting large numbers of these fundamental devices, we can construct a computer

![](Picture2.jpg)

<!-- Slide number: 20 -->
# Evolution of Computers
Four basic functions could be related to these two components as follows:
Data storage: Provided by memory cells
Data processing: Provided by gates
Data movement: The paths among components are used to move data from memory to memory and from memory through gates to memory
Control: The paths among components can carry control signals
For example, a gate will have one or two data inputs plus a control signal input that activates the gate
When the control signal is ON, the gate performs its function on the data inputs and produces a data output
Similarly, the memory cell will store the bit that is on its input lead when the WRITE control signal is ON and will place the bit that is in the cell on its output lead when the READ control signal is ON
The integrated circuit exploits the fact that such components can be fabricated from a semiconductor such as silicon (Si)

<!-- Slide number: 21 -->
# Relationship Among Wafer, Chip, and Gate

![](Picture2.jpg)

<!-- Slide number: 22 -->
# Fabrication of Integrated Circuits
A thin wafer of silicon is divided into a matrix of small areas, each a few millimeters square
The identical circuit pattern is fabricated in each area, and the wafer is broken up into chips
Each chip consists of many gates and/or memory cells plus a number of input and output attachment points
This chip is then packaged in housing that protects it and provides pins for attachment to devices beyond the chip
A number of these packages can then be interconnected on a printed circuit board to produce larger and more complex circuits

<!-- Slide number: 23 -->
# Fabrication of Integrated Circuits
Initially, only a few gates or memory cells could be reliably manufactured and packaged together
These early integrated circuits are referred to as small-scale integration (SSI)
As time went on, it became possible to pack more and more components on the same chip
And so comes the terms- LSI, MSI, VLSI and ULSI

<!-- Slide number: 24 -->
# Moore’s law

![](Picture2.jpg)

<!-- Slide number: 25 -->
# Moore’s law
The consequences of Moore’s law are profound:
The cost of a chip has remained virtually unchanged during this period of rapid growth in density
This means that the cost of computer logic and memory circuitry has fallen at a dramatic rate
Because logic and memory elements are placed closer together on more densely packed chips, the electrical path length is shortened, increasing operating speed.
The computer becomes smaller, making it more convenient to place in a variety of environments
There is a reduction in power and cooling requirements
The interconnections on the integrated circuit are much more reliable than solder connections
With more circuitry on each chip, there are fewer inter-chip connections

<!-- Slide number: 26 -->
# Comparison – Among Generations

![](Picture2.jpg)

<!-- Slide number: 27 -->
# PERFORMANCE ASSESSMENT
In evaluating processor hardware and setting requirements for new systems, following parameters are important
Performance (key parameter)
Cost
Size
Security
Reliability
Power consumption
Difficult to make meaningful performance comparisons
Should make use of traditional performance measures

<!-- Slide number: 28 -->
# Clock Speed and Instructions per Second
THE SYSTEM CLOCK
Operations performed by a processor, such as fetching an instruction, decoding the instruction, performing an arithmetic operation, and so on, are governed by a system clock. Typically, all operations begin with the pulse of the clock.
The speed of a processor is dictated by the pulse frequency produced by the clock, measured in cycles per second, or Hertz (Hz)
Typically, clock signals are generated by a quartz crystal, which generates a constant signal wave while power is applied
This wave is converted into a digital voltage pulse stream that is provided in a constant flow to the processor circuitry
For example, a 1-GHz processor receives 1 billion pulses per second
The rate of pulses is known as the clock rate, or clock speed
One increment, or pulse, of the clock is referred to as a clock cycle, or a clock tick
The time between pulses is the cycle time

<!-- Slide number: 29 -->
# Clock Speed and Instructions per Second

![](Picture2.jpg)

<!-- Slide number: 30 -->
# Clock Speed and Instructions per Second
The execution of an instruction involves a number of discrete steps, such as-
fetching the instruction from memory, decoding the various portions of the instruction, loading and storing data, and performing arithmetic and logical operations
Thus, most instructions on most processors require multiple clock cycles to complete
Some instructions may take only a few cycles, while others require dozens
A straight comparison of clock speeds on different processors does not tell the whole story about performance

<!-- Slide number: 31 -->
# Clock Speed and Instructions per Second

<!-- Slide number: 32 -->
# Clock Speed and Instructions per Second
Let      be the number of cycles required for instruction type i and  be the number of executed instructions of type i for a given program
Then we can calculate an overall CPI as follows:

<!-- Slide number: 33 -->
# Clock Speed and Instructions per Second
The processor time T needed to execute a given program can be expressed as:

We can refine this formulation by recognizing that during the execution of an instruction, part of the work is done by the processor, and part of the time a word is being transferred to or from memory
In this latter case, the time to transfer depends on the memory cycle time, which may be greater than the processor cycle time
We can rewrite the preceding equation as

where p is the number of processor cycles needed to decode and execute the instruction, m is the number of memory references needed, and k is the ratio between memory cycle time and processor cycle time
The five performance factors in the preceding equation (Ic, p, m, k, τ ) are influenced by four system attributes: the design of the instruction set (known as instruction set architecture), compiler technology (how effective the compiler is in producing an efficient machine language program from a high-level language program), processor implementation, and cache and memory hierarchy

<!-- Slide number: 34 -->
# Clock Speed and Instructions per Second
For the multi-cycle MIPS, there are 5 types of instructions:
Load (5 cycles)
Store (4 cycles)
R-type (4 cycles)
Branch (3 cycles)
Jump (3 cycles)
If a program has:
50% load instructions
15% R-type instructions
25% store instructions
8% branch instructions
2% jump instructions
then, the CPI is:

<!-- Slide number: 35 -->
# Clock Speed and Instructions per Second
A 400-MHz processor was used to execute a benchmark program with the following instruction mix and clock cycle count:
Instruction type Instruction count Clock cycle count Integer arithmetic 45000 1 Data transfer 32000 2 Floating point 15000 2 Control transfer 8000 2
Total instruction count = 100000
Determine the effective CPI, MIPS rate, and execution time for this program.

<!-- Slide number: 36 -->
# Clock Speed and Instructions per Second

<!-- Slide number: 37 -->
# Clock Speed and Instructions per Second
A common measure of performance for a processor is the rate at which instructions are executed, expressed as millions of instructions per second (MIPS), referred to as the MIPS rate
We can express the MIPS rate in terms of the clock rate and CPI as follows:

Consider the execution of a program which results in the execution of 2 million instructions on a 400-MHz processor
The program consists of four major types of instructions
The instruction mix and the CPI for each instruction type are given below based on the result of a program trace experiment

<!-- Slide number: 38 -->
# Clock Speed and Instructions per Second

![](Picture2.jpg)

<!-- Slide number: 39 -->
# Clock Speed and Instructions per Second
Another common performance measure deals only with floating-point instructions
These are common in many scientific and game applications
Floating point performance is expressed as millions of floating-point operations per second (MFLOPS), defined as follows:

![](Picture3.jpg)

<!-- Slide number: 40 -->
# Benchmarks
Measures such as MIPS and MFLOPS have proven inadequate to evaluating the performance of processors
Because of differences in instruction sets, the instruction execution rate is not a valid means of comparing the performance of different architectures
RISC and CISC machines may not be rated with same MIPS rating but may do same amount of work at the same time
Moreover, the performance of a given processor on a given program may not be useful in determining how that processor will perform on a very different type of application

### Notes:
The CISC approach attempts to minimize the number of instructions per program, sacrificing the number of cycles per instruction. RISC does the opposite, reducing the cycles per instruction at the cost of the number of instructions per program.

<!-- Slide number: 41 -->
# Amdahl’s Law
First proposed by Gene Amdahl
Deals with the potential speedup of a program using multiple processors compared to a single processor
Consider a program running on a single processor such that a fraction (1 - f) of the execution time involves code that is inherently serial and a fraction f that involves code that is infinitely parallelizable with no scheduling overhead
Let T be the total execution time of the program using a single processor
Then the speedup using a parallel processor with N processors that fully exploits the parallel portion of the program is as follows:

<!-- Slide number: 42 -->
# Amdahl’s Law

Two important conclusions can be drawn:
When f is small, the use of parallel processors has little effect
As N approaches infinity, speedup is bound by 1/(1 - f), so that there are diminishing returns for using more processors

<!-- Slide number: 43 -->
# Amdahl’s Law
Amdahl’s law can be generalized to evaluate any design or technical improvement in a computer system
Consider any enhancement to a feature of a system that results in a speedup
The speedup can be expressed as:

<!-- Slide number: 44 -->
# Amdahl’s Law

<!-- Slide number: 45 -->
# Amdahl’s Law
 Suppose that a task makes extensive use of floating-point operations, with 40% of the time is consumed by floating-point operations. With a new hardware design, the floating-point module is speeded up by a factor of 10. What is the overall speedup?

<!-- Slide number: 46 -->
# Thank you!