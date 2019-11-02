# Based on pycommon v0.5

PROJ="color_logger"
COLOR="\033[31m"
RESET="\033[0m"

rm -r .ci/output/
mkdir -p .ci/output/

grep -i -r --exclude-dir="__pycache__" "TODO" ./ \
    | grep -v "grepping for TODOs" \
    | grep -v "anybadge -l TODOs" \
    | grep -v "\.pip" \
    | grep -v "\.ci/" \
    | grep -v "\.git" > .ci/output/todos.txt

TODOS=$(cat .ci/output/todos.txt | wc -l)

anybadge -l TODOs -f .ci/output/todos.svg -m "%.0f" \
         -v=$TODOS 1=green 4=yellow 8=orange 16=red;
echo "$COLOR TODOs: $RESET"
cat .ci/output/todos.txt

pylint --output-format=text $PROJ > .ci/output/pylint.txt
RATING=$(cat .ci/output/pylint.txt | sed -n \
         's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p')
anybadge -l pylint -f .ci/output/pylint.svg \
         -v=$RATING 4=red 6=yellow 8=orange 10=green;
echo "$COLOR Lint Rating: $RESET $RATING"

mypy --strict . | grep -v "Success: " > .ci/output/mypy.txt
mypy_out=$(cat .ci/output/mypy.txt | wc -l)
anybadge -l mypy -f .ci/output/mypy.svg -m "%.0f" \
         -v=$mypy_out 1=green 5=yellow 10=orange 15=red
echo "$COLOR MyPy Issues: $RESET"
cat .ci/output/mypy.txt 

PYTHONPATH="./" pytest --cov-report term-missing --cov=$PROJ \
          > .ci/output/coverage.txt

cov=$(coverage report | grep "TOTAL" | \
          awk '{print substr($4, 1, length($4)-1)}')
anybadge -l coverage -f .ci/output/coverage.svg -v \
         $cov 20=red 40=orange 80=yellow 100=green
echo "$COLOR Total Coverage: $RESET $cov"



