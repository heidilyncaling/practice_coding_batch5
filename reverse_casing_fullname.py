BEGIN
    PRINT "Full name:"  
    INPUT fullname  

    FOR each character in fullname DO  
        IF character is uppercase THEN  
            Convert character to lowercase  
        ELSE  
            Convert character to uppercase  
        ENDIF  
    ENDFOR  

    PRINT fullname  
END