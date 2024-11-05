RE chal by jiapoh

![image](https://github.com/user-attachments/assets/e96edbb5-f296-4dfc-8742-360fd53f8118)
The challenge will require us to download a file

![image](https://github.com/user-attachments/assets/b1bfae1f-37e5-4e40-8d0b-1349261e920b)
Open file in VS code, most of the words is unreadable but there is a key word in the top right corner, from this we can know this is an ELF file
So is time to ghidra it. (ghidra - A tool used for RE)

![image](https://github.com/user-attachments/assets/01b3776d-20d2-4d28-a86e-6151f01ad0db)
Look at main function first, everything looks normal except for the xoring() function. 

![image](https://github.com/user-attachments/assets/e8de0769-6fff-4295-bbbc-08294719c474)
Navigate to xoring() function, we can see the xor formula there ,the formula involves xor local_1f, local_29,int local_10 and int local_c.
From the formula we can see evrything is converted into bytes with the (byte *) then xor is performed.
To understand the program i run it in kali and get this output(picture below). 

![image](https://github.com/user-attachments/assets/a4f272c4-a5f0-46f4-803b-050f5c4437eb)
The program just output a weird string. 
So here is the whole process after looking at the code, the program will take local_1f(fZjkMyeQWVmmbk) XOR with the local_29(123456789, you can get this can converting hex to ASCII)

And here is the flag
![image](https://github.com/user-attachments/assets/53bea60d-71de-4de1-aeda-3137f43e94a1)

**FLAG**

WhY_xORing_^V^
