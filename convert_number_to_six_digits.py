BEGIN
    Print "Enter number (0-1000):"
    INPUT number

     Set zeros_needed to 6 minus the length of number  
    Set padded_number to zeros_needed times "0" + number  

    PRINT "Output: ", padded_number  
END  