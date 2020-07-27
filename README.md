# DiZer 3

```dizer3``` is a discoursive analyzer for Brazilian Portuguese. It is under development...

### Installation

- Clone this repository
```git clone https://github.com/egmaziero/dizer3.git```.   

- Install dependencies (installing inside a virtual environment is advisable...)
```pip install -r requirements.txt```.

- Download models using the link: https://drive.google.com/file/d/1z9WuR5USFHrangVNGpvMEA2oyjlGob8A/view?usp=sharing. Extract the directory ```models```and put it in ```dizer3``` directory.
 

### Basic usage
```dizer3``` performs discourse (based on Rhetorical Structure Theory) analysis on raw text files. 

To run the parser use:

```python3 dizer3\run_pipeline.py --f file_path ```

or 

```python3 dizer3\run_pipeline.py --d directory_path```

where 

- ```--f``` indicates the a raw text file path. This argument takes precedence over ```-d```
- ```--d``` indicates the directory with raw text files to be analyzed

### Citation

To cite this work, use one of the following reference:

> Maziero, E.G.; Hirst, G.; Pardo, T.A.S. (2015). Semi-Supervised Never-Ending Learning in Rhetorical Relation Identification. In the _Proceedings of the Recent Advances in Natural Language Processing - RANLP_, pp. 436-442. September 5-11. Hissar/Bulgaria.

>Maziero, E. G. (2016). _Análise retórica com base em grande quantidade de dados._ Tese de Doutorado, Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo, São Carlos. doi:10.11606/T.55.2017.tde-13012017-103446. Recuperado em 2020-06-10, de www.teses.usp.br

