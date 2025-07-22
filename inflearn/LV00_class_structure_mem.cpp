#include <cstring>
#include <iostream>
using namespace std;
/* default 접근제한 지정자 private */
class cPeople
{
    public:
        int age;
        int height;
        void AddAge(/*People const this*/)
        {
            /* (*this) */age += 1;
            /* this = 0x12345678 */
        }    
        char name[20];
};

/* default 접근제한 지정자 public */

struct People
{
    public:
        int age;
        int height;
        char name[20];
};

void AddAge(People* p1)
{
    (*p1).age += 1;
}

int main()
{
    People sujin;
    sujin.age = 31;
    strcpy(sujin.name/*&sujin.name[0]*/, "SujinYu");
    AddAge(&sujin);
    cout<< "Sujin's age: " << sujin.age << endl;

    cPeople manjae;
    manjae.age = 30;
    strcpy(manjae.name/*&manjae.name[0]*/, "ManjaeCho");
    manjae.AddAge(/*&manjae*/);
    cout << "Manjae's age: " << manjae.age << endl;

    const int number1 = 10;
    // number1 = 20; // 오류: number1는 상수이므로 값을 변경할 수 없다.
    cout << "Number1: " << number1 << endl; // 출력: Number1: 10

    int number2 = 10;
    int* const pcNumber2 = &number2; // pcNumber2는 상수 포인터이므로, pcNumber2가 가리키는 주소는 변경할 수 없다.
    // p = &number; // pNumber는 상수 포인터이므로, pNumber가 가리키는 주소는 변경할 수 없다.
    *pcNumber2 = 20; // pcNumber2가 가리키는 값은 변경할 수 있다.
    cout << "Number: " << number2 << endl; // 출력: Number: 20

    const int* cpNumber2 = &number2; // cpNumber2는 상수 포인터이므로, cpNumber2가 가리키는 주소는 변경할 수 없다.
    int anotherNumber = 30;
    cpNumber2 = &anotherNumber; // cpNumber2가 가리키는 주소를 변경할 수 없다.
    // *cpNumber2 = 40; // 오류: cpNumber2가 가리키는 값은 상수이므로 변경할 수 없다.
    cout << "Another Number: " << *cpNumber2 << endl; // 출력: Another Number: 30

    const int* const cpcNumber2 = &number2; // cpcNumber2는 상수 포인터이므로, cpcNumber2가 가리키는 주소와 값 모두 변경할 수 없다.
    // cpcNumber2 = &anotherNumber; // 오류: cpcNumber2가 가리키는 주소는 변경할 수 없다.
    // *cpcNumber2 = 50; // 오류: cpcNumber2가 가리키는 값은 상수이므로 변경할 수 없다.
    cout << "CPC Number: " << *cpcNumber2 << endl; // 출력: CPC Number: 20

    return 0;
}
