# Ejemplos de código
## MODELOS - `models.py`
### Lista desplegable
```python
tierra=models.CharField(
  max_length=3,
  choices=[
    ('TIE',"Tierra"),
    ('ARE',"Arenosa"),
    ('ARC',"Arcillosa"),
    ('LIM',"Limosa"),
    ('TUB',"Turba"),
    ('TIZ',"Tiza")
  ],
  default='TIE'
)
```