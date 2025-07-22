#include <cstring>
#include <iostream>
using namespace std;
/* default 접근제한 지정자 private */
class cPeople
{
    public:
        int age;
        int height;
    private:
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
    strcpy(sujin.name, "SujinYu");
    AddAge(&sujin);
    cout<< "Sujin's age: " << sujin.age << endl;

    cPeople manjae;
    manjae.age = 30;
    return 0;
}
