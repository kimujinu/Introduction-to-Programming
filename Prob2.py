import random                                                      #라이브러리 가져오기

input_number = int(input("복권번호를 입력하시오(10에서 99사이): ")) #정수형타입으로 복권번호를 입력받습니다.
random_number = random.randint(10,99)                              # 10부터 99까지의 당첨번호를 random_number 변수에 넣습니다.


random_number_tens_digit = random_number//10                       #당첨번호의 십의 자릿수를 구합니다.
random_number_of_digits = random_number%10                         #당첨번호의 일의 자리수를 구합니다. 

input_number_tens_digit = input_number//10                         #입력번호의 십의 자릿수를 구합니다.
input_number_of_digits = input_number%10                           #입력번호의 일의 자리수를 구합니다. 


print("당첨번호는",random_number,"입니다.")                         #당첨번호를 출력합니다.

if random_number == input_number :                                  #입력번호와 당첨번호가 똑같으면 아래의 소스코드를 실행합니다.
    print("상금은 100만원 입니다.축하합니다!")                      # 위의 조건이 참이면 소스코드를 실행합니다.
elif (random_number_tens_digit == input_number_tens_digit or random_number_of_digits ==input_number_of_digits) : #당첨번호의 십의자리와 입력번호의 십의자리, 당첨번호의 일의자리와 입력번호의 일의자리를 서로 같은지 비교하여 2개의 조건중 한개라도 해당된다면 아래의 소스코드를 실행합니다.
    print("상금은 50만원 입니다.축하합니다!")                        # 위의 조건중 하나라도 참이 있다면 소스코드를 실행합니다.
else :                                                              #위의 조건 두개가 참이 아니라면 아래의 소스코드를 실행합니다.
    print("상금은 없습니다.")                                       #위의 조건 두개가 참이 아니라면 소스코드를 실행합니다.
