from asyncio import create_task,wait,run
from colorama import Fore,Back,Style
from sys import exit,argv
from os import name,system
from re import match








class get_event_loopx(object):

    def __init__(self,tasks=str(),out=str(),count=int(),error=int()) -> None:
        self.tasks = tasks
        self.out   = out
        self.count = 0
        self.error = 0
        pass

    def p_green(self,string):
        print(Fore.GREEN + Style.BRIGHT + string + Fore.RESET + Style.RESET_ALL)

    def p_red(self,string):
        print(Fore.RED + Style.BRIGHT + string + Fore.RESET + Style.RESET_ALL)

    async def p_white(self,string):
        print(Fore.WHITE + Style.BRIGHT + string + Fore.RESET + Style.RESET_ALL)

    async def clear(self):
        command = 'clear'
        if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        system(command)

    def read(self,filex):
        RETURNAS = []
        ii = open(filex, 'r', encoding="ISO-8859-1")
        obj = ii.readlines()
        for i in obj:
            RETURNAS.append(i.rstrip('\n\r'))
        return RETURNAS

    def write(self,line):
        ii = open(self.out, 'a', encoding="ISO-8859-1")
        ii.write(line + '\n')
        ii.close()

    async def func(self,s):

        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if match(pat, s):
            self.write(s)
            self.count+=1
            self.p_green(f'{self.count}|FOUND|{self.count}')
        else:
            self.error+=1
            self.p_red(f'{self.error}|ERROR|{self.error}')

    async def main(self):
        self.file_in = self.read(self.tasks)
        for ii in self.file_in:
            xyz = create_task(self.func(ii))

        await wait([print(ii) for ii in xyz])












def main(filex,out_file):
    try:
        obj    = get_event_loopx(tasks=filex,out=out_file)
        runner = obj.main()

        run(runner)
    except Exception as iii:
        print(iii)
        run(obj.clear())
        run(obj.p_white(f'CORRECT FORMAT FOUND : {obj.count}\n\nNONE FORMAT FOUND : {obj.error}'))





if __name__ == '__main__':
    try:
        main(filex=argv[1],out_file=argv[2])
    except IndexError:
        print('\n\npython <namefile.py> <file_to_scan.py>\n\n')


