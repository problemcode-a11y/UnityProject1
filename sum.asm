PAGE 60,132
TITLE PGM1
;******************************************************
; PGM1 TITLE: SAMPLE PROGRAM TO ADD COST TO TOTAL     *
; PROGRAMMER: Cornel Doyle                          *
; PURPOSE: ADD TWO WORD-NUMBERS                       *
;******************************************************
; PROGRAM CODE SEGMENT
PGM1CD SEGMENT
MAIN   PROC     FAR
;HOUSEKEEPING SECTION
       
       ASSUME   CS:PGM1CD,DS:PGM1DA,SS:PGM1SK
       MOV      AX,PGM1DA    ; ESTABLISH ADDRESSABILITY
       MOV      DS,AX        ; TO PGM1DA - THE PGM'S DATA SEGMENT
;MAIN PROCESS SECTION
       
       MOV      AL,a         ; REG AL = a
       ADD      AL,b         ; ADD b TO AL
       ADD      AL,c
       ADD      AL,d
       ADD      AL,e
       MOV      f,AL         ; STORE SUM TO f
; RETURN TO DOS SECTION
       
       MOV      AL,0         ; SET 0 AS THE RETURN CODE FOR DOS
       MOV      AH,4CH       ; SET FOR DOS END PROCESS FUNCTION
       INT      21H          ; CALL DOS TO END PROGRAM
MAIN   ENDP
PGM1CD ENDS
;PROGRAM DATA SEGMENT
PGM1DA SEGMENT
a      DB       1
b      DB       2
c      DB       3
d      DB       4
e      DB       5
f      DB       0
PGM1DA ENDS
;PROGRAM STACK SEGMENT
PGM1SK SEGMENT PARA STACK 'STACK'
       
       DW       32 DUP (?)
PGM1SK ENDS
       END