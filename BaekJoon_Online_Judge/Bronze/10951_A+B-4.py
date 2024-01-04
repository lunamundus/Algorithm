while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
    
'''
EOF(End Of File) 이용
- 파일의 끝을 표현하기 위해 정의한 상수(-1)
- 함수가 파일의 끝에 도달하거나 Ctrl+Z 후 Enter로 종료할 때만 반환
- 각 언어마다 EOF를 읽는 방법은 차이가 있음
- Python에서는 try~except를 사용하여 EOFError를 예외처리하여 코드 실행이 중단되는 것을 방지
- try에서는 본래 실행하려는 코드를 실행하고, except는 error가 발생했을 때(즉 EOF일때) 반복문을 종료하도록 설정하여 문제 해결 가능
'''
