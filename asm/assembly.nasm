;programa que printa na tela e executa o arquivo tag

global _start
section .text

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg	;msg eh o endereco, algo como &msg em c
    mov rdx, 33
    syscall

    mov rax, 59
    mov rdi, tag	;tag eh o endereco, algo como &tag em c
    mov rsi, null_byte		
    mov rdx, null_byte
    syscall

    mov rax, 60	; codigo de saida	
    mov rdi, 0		;retorno 0 = saiu com sucesso
    syscall


section .data
msg:
    db "bem vindo ao meu codigo assembly",0xa		;0xa = \n (em hexadecimal)
    
tag:
    db "./tag", 0x00	; necessario passar o caracter de fim de texto
    
null_byte: 
    db 0
