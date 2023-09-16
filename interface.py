import tkinter as tk
import main


window = tk.Tk()
window.title('Text Analyser')
window.geometry('1920x1080')


# назначение функций
def create_checkbutton(parts_of_speech: list, grammemes: list) -> dict:
    for_parts_of_speech = {}
    for num in range(len(parts_of_speech)):
        for_parts_of_speech[parts_of_speech[num]] = [tk.IntVar(), grammemes[num]]
        packs[parts_of_speech[num]] = tk.Checkbutton(text=parts_of_speech[num], variable=for_parts_of_speech[parts_of_speech[num]][0])
    return for_parts_of_speech


def checkbutton_morphy() -> list:
    parts_of_speech_checkbuttom = []
    for key in for_parts_of_speech.keys():
        print(for_parts_of_speech[key][0].get())
        if for_parts_of_speech[key][0].get():
            parts_of_speech_checkbuttom.append(for_parts_of_speech[key][1])
            print(for_parts_of_speech[key][1])
    return parts_of_speech_checkbuttom


def path_to_file():
    grammenes = checkbutton_morphy()
    print(grammenes)
    text_analyser = main.TextAnalyser(source_file=packs['path_to_file_entry'].get(), parts_of_speech=grammenes)


packs = {}
# ввод пути к файлу
packs['path_to_file_lable'] = tk.Label(text='Введите имя файла:', font=("Arial", 14))
packs['path_to_file_entry'] = tk.Entry(width=30, font=1)

# выбор частей речи

packs['morphy_lable'] = tk.Label(text='Выберите части речи:', font=("Arial", 12))
for_parts_of_speech = create_checkbutton([
    'Существительные',
    'Прилагательные(полное)',
    'Прилагательные(краткое)',
    'Компаративы',
    'Глаголы(личная форма)',
    'Глаголы(инфинитив)',
    'Причастия(полное)',
    'Причастия(кратко)',
    'Деепричастия',
    'Числительные',
    'Наречия',
    'Местоимения',
    'Предактивы',
    'Предлоги',
    'Союзы',
    'Частицы',
    'Междометия'
], [
    'NOUN',
    'ADJF',
    'ADJS',
    'COMP',
    'VERB',
    'INFN',
    'PRTF',
    'PRTS',
    'GRND',
    'NUMR',
    'ADVB',
    'NPRO',
    'PRED',
    'PREP',
    'CONJ',
    'PRCL',
    'INTJ'
])

packs['path_to_file_buttom'] = tk.Button(text='Провести анализ текста', command=path_to_file)

for item in packs.items():
    item[1].pack(anchor='nw', padx=5, pady=2)




window.mainloop()