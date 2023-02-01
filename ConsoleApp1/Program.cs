using System;
using System.Runtime.CompilerServices;
using System.Text;




    Console.InputEncoding = Encoding.Unicode;
    Console.OutputEncoding = Encoding.Unicode;

/*string name;
int age;
Console.Write("Введите ваше имя: ");
name = Console.ReadLine();
Console.Write("Введите ваш возраст: ");
age = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"Вас зовут {name} и вам {++age} год.");
*/

float health = 100;
int levelHero = 1;
int armor = 50;
int armorEnemy = 50;
int strngeHero = 30;
float healthEnemy = health * levelHero / 2;
float damageEnemy = 66 * levelHero / 2;
int precent = 100;
string action;
string chapter = "New Game";


    

 void statusHero() {
    Console.Write($"You\n" +            
        $"HP - {health}\n" +     
        $"ARM - {armor}\n" +  
        $"STR - {strngeHero} \n\n");
}

void statusEnemy() {
    Console.Write($"Enemy\n" +
         $"HP - {healthEnemy} \n" +
         $"ARM - {armorEnemy} \n" +
         $"STR - {damageEnemy} \n\n");
}


/*
 нужен многомерный массив, [[1(hero), 1(hp), 1(arm), 1(str)]
                            [2(enemy), 2(hp), 2(arm), 2(str)]       
                            [3(enemy), 3(hp), 3(arm), 3(str)]       
                            [4(enemy), 4(hp), 4(arm), 4(str)]]     
показ уровня +
отмена драк после смерти врага -
восстановление здоровья полсе победы -
кнопку продолжить -
начинать занво цикл -
запускать занво цикл по нажатию кнопки -
 
 
 */


while (true)
{

    switch (chapter)
    {
        case "New Game":
            Console.Clear();
            Console.Write("Приветсвую восркеcший. Ты герой или еще один мешок с костями?\n" +
                "Покажи на что способен!\n\n" +
                "| Start - войти в подземелье | Exit - выйти |\n");
            chapter = Console.ReadLine();
            break;
        case "Exit":
            Console.Clear();
            Console.Write("Испытай удачу в следующий раз!\n");
            Environment.Exit(0);
            break;
        case "Start":
            Console.Clear();
            Console.Write("И так сынок, это твой первый бой. сейчас я тебе помогу, а дальше давай сам.\n" +
                "ИНФО:\nПервым представляется инфо о тебе, а вторым твоего  врага.\n" +
                "БОЙ:\nЗначит так, у тебя есть пока 3 варианта. Attack - занчит ты нападешь на врага,\n" +
                "но не забывай, что унего как и у тебя есть защита. А еще после твоего удара, враг атакует тебя.\n" +
                "Block - блокировать удар, правильно подумал. урона пройдет по тебе меньше, да и ты сможешь накопить\n" +
                "сил и ударить в следующий раз сильнее. И наконец то команда Exit, никто не запрщает тебе сбежать\n" +
                "поджав хвост. Помни, что всегда придется начинать сначала. Чтож, удачи!\n" +
                "| Fight | Exit |\n");
            chapter= Console.ReadLine();
            break;
        case "Fight":
            Console.Clear();
            statusHero();
            statusEnemy(); 
            Console.Write("Выберите дальнейшие действие:\n" +
            "| Attack | Block | Exit |\n");
            action = (Console.ReadLine());
            switch (action)
            {
                case "Attack":
                    Console.Clear();
                    healthEnemy -= strngeHero * armorEnemy / precent;
                    Console.Write("Вы атакуете врага, а затем он атакует вас.\n");
                    health -= damageEnemy * armor / precent;
                    statusHero();
                    statusEnemy();
                    break;

                case "Block":
                    Console.Clear();
                    Console.Write("Вас атакуют, а вы защищаетесь.\n");
                    health -= (armor - damageEnemy);
                    strngeHero += 5;
                    statusHero();
                    statusEnemy();
                    break;

                case "Exit":
                    chapter = "Exit";
                    break;

                default:
                    Console.Clear();
                    Console.Write("Нет такой команды, ты слепой? Начинай занаво.\n" +
                        "| New Game | Exit |\n");
                        chapter = Console.ReadLine();
                    break;


            }
            if (health <= 0)
            {
                Console.Clear();
                Console.WriteLine("Ты погиб.\n" +
                    "| New Game | Exit |");
                chapter = Console.ReadLine();
            }
            else if (healthEnemy <= 0)
            {
                Console.Clear();
                statusHero();
                Console.Write("Ты победил! LVL - 2\nВсе параметры увеличены на 5 единиц.\n" +
                    "| Next Enemy | Exit |\n");
                health = 100 + 5;
                strngeHero += 5;
                armor += 5;
                
                chapter = Console.ReadLine();
            }
            break;
        case "Next Enemy":
            //сделай тут цикл на рандомного злодея с рандомными параметрами и разными фразами и тип когда 10 битв пройдет, то начнется босфайт
            break;
        case "Boss Fight":
            break;
        case "4":
            break;
        case "5":
            break;
        case "6":
            break;
        case "7":
            break;
            default:
            Console.Clear();
            Console.Write("Ты что пытаешься сделать?\n" +
                "Соре, но тут ток новая игра.\n" +
                "| New Game | Exit |\n");
            chapter = Console.ReadLine();
            break;
    }
   
    
}
    
    




/*Console.Write("Введите здовроье:");
health = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите броню:");
armor = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите урон:");
damage = Convert.ToInt32(Console.ReadLine());

health -= Convert.ToSingle(damage) / armor * precent;

Console.WriteLine($"Вам нанесли {damage} урона, у вас отсалось {health} здоровья");

*/