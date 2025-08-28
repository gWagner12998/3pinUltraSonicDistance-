# 3pinUltraSonicDistance-
A small python library created for a 3 pin ultra sonic distance sensor or PING))) ultra sonic distance sensor. It measures distance, then converts it into desired unit.

## Download 
```bash
git clone https://github.com/gWagner12998/3pinUltraSonicDistance-.git
```
## Setup
Check the example file to see how to use the library.

### Importing
```python
from Ultra_Sonic import UltraSonic
```
### Selecting Pin
RPi.GPIO has two modes BCM or BOARD
```python
sensor=UltraSonic(18,'BOARD','mm')
sensor=UltraSonic(24,'BCM','mm')
```
### Selecting Unit
When selecting unit you can abbreviate or spell it out. There are six units to choose from-in, ft, yrd, mm, cm, m.
```python
sensor=UltraSonic(18,'Board','mm')
sensor=UltraSonic(18,'Board','milimeter')
```
 

