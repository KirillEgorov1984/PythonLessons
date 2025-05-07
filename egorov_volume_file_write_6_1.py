# запись в файл
def main_write():
    outfile = open('philosophers.txt', 'w', encoding='utf-8')

    outfile.write('Джон Локк\n')
    outfile.write('Дэвид Хьюм\n')
    outfile.write('Эдмунд Берк\n')

    outfile.close()

if __name__ == '__main__':
    main_write()

# чтение записей из файла
def main_read():
    infile = open('philosophers.txt', 'r', encoding='utf-8')
    infile_read = infile.read()
    infile.close()
    #print(infile_read)

if __name__ == '__main__':
    main_read()

#построчное чтение файла
def main_read_rows():
    infile = open('philosophers.txt', 'r', encoding='utf-8')
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')


    infile.close()
    print(line1, line2, line3)

if __name__ == '__main__':
    main_read_rows()

