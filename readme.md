# Menti_bot

Is used to vote equally many times for a certain menti quiz. Average of 11 seconds per vote.
Use threading to get average of 2 seconds per vote.

## Usage
Set correct data in data.py
```python
menti_code = 123456
total_votes = 3
```
Run application from main.py
```commandline
py
from main import vote_for_option, auto_equal_vote, thread_function
vote_for_option(0)
auto_equal_vote()
thread_function(vote_for_option, 0)
```

