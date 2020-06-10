# DiZer 3

```dizer3``` is a discoursive analyzer for Brazilian Portuguese.

### Installation

- Clone this repository:
```git clone https://github.com/egmaziero/cstparser.git```.   

- Install dependencies using

```pip install -r requirements.txt```.
 

### Basic usage
```dizer3``` performs discourse (based on Rhetorical Structure Theory) analysis on raw text files. 

To run the parser use:

```python3 dizer3\run_pipeline.py --f file_path  -- s True/False```

or 

```python3 dizer3\run_pipeline.py --d directory_path  -- s True/False```

where 

- ```--f``` indicates the a raw text file path. This argument takes precedence over ```-d```
- ```--d``` indicates the directory with raw text files
- ```--s``` is a boolean value (True or False) indicating if structural segments/relations will be considered. Default is True. See more detais in the thesis referenced below.

### Citation

To cite this work, use one of the following reference:

>ISO
MAZIERO, Erick Galani. _Análise retórica com base em grande quantidade de dados_ [doi:10.11606/T.55.2017.tde-13012017-103446]. São Carlos : Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, 2016. Tese de Doutorado em Ciências de Computação e Matemática Computacional. [acesso 2020-06-10].

>ABNT
MAZIERO, Erick Galani. **Análise retórica com base em grande quantidade de dados.** 2016. Tese (Doutorado em Ciências de Computação e Matemática Computacional) - Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, São Carlos, 2016. doi:10.11606/T.55.2017.tde-13012017-103446. Acesso em: 2020-06-10.

>APA
Maziero, E. G. (2016). _Análise retórica com base em grande quantidade de dados._ Tese de Doutorado, Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, São Carlos. doi:10.11606/T.55.2017.tde-13012017-103446. Recuperado em 2020-06-10, de www.teses.usp.br

>Vancouver
Maziero, Erick Galani. Análise retórica com base em grande quantidade de dados [tese]. São Carlos: , Instituto de Ciências Matemáticas e de Computação; 2016 [citado 2020-06-10]. doi:10.11606/T.55.2017.tde-13012017-103446.

