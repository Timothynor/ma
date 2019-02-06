#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <conio.h>
using namespace std;
#define KEY_UP 72
#define KEY_DOWN 80 
#define KEY_LEFT 75
#define KEY_RIGHT 77

class player{
    public:
        int attack = 20;
        int health = 100;
        int defence = 40;
        bool pdtaken = false;
};
class monster{
    const int defence;
    const bool monsterhit;
    const bool dtaken;
    public:
        const int gold_drop = rand() % 10;
        const int hp = 100;
        bool monsterdead = false;
        /*this is the list so I can call the values*/
        monster():defence(40),monsterhit(false), dtaken(false) {}
        player obj1;
        void harmmonster(){
            if(monsterhit == true){
                cout<<obj1.attack - hp<<endl;
            }
        }
        void killmonster(){
            if(hp <= 0){
                monsterdead == true;
            }
            if(hp <= 0 && monsterdead == true){
            
            }
        }
};
class cards{
    public:
        int fire = 20;
        int ice = 20;
        int wind = 20;
        int water = 20;
        monster obj;
        void fireD(){
            cout << fire - obj.hp<<endl;
        }
        void iceD() {
            cout<<ice - obj.hp<<endl;
        }
        void windD() {
            cout<<wind - obj.hp<<endl;
        }
        void waterD() {
            cout<<water - obj.hp<<endl;
        }
        void attackmonster() {
            int c = 0;
            switch((c=getch())){
                case KEY_UP:
                    fireD();
                    break;
                case KEY_DOWN:
                    iceD();
                    break;
                case KEY_LEFT:
                    windD();
                    break;
                case KEY_RIGHT:
                    waterD();
                    break;
            }
        }
};
int main()
{
    cards mon;
    mon.attackmonster();
    player obj;
    bool gameover = false;
    if(gameover = true && obj.health == 100){
        for(obj.health = 100; obj.health <= 0; obj.health = obj.health - 100);
    }
    monster obj2;
    if(obj2.monsterdead = true){
        cout<<obj2.gold_drop<<endl;
    }
    return 0;
}




