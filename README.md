# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/en0mia/stuquiz-api/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                           |    Stmts |     Miss |   Cover |   Missing |
|--------------------------------------------------------------- | -------: | -------: | ------: | --------: |
| app/\_\_init\_\_.py                                            |        0 |        0 |    100% |           |
| app/stuquiz/\_\_init\_\_.py                                    |       23 |       17 |     26% |     14-41 |
| app/stuquiz/controllers/\_\_init\_\_.py                        |        0 |        0 |    100% |           |
| app/stuquiz/controllers/abstract\_controller.py                |        6 |        1 |     83% |        17 |
| app/stuquiz/controllers/admin/\_\_init\_\_.py                  |        0 |        0 |    100% |           |
| app/stuquiz/controllers/admin/login\_admin\_controller.py      |       18 |        0 |    100% |           |
| app/stuquiz/controllers/admin/logout\_admin\_controller.py     |       12 |        0 |    100% |           |
| app/stuquiz/entities/admin.py                                  |       11 |        0 |    100% |           |
| app/stuquiz/entities/answer.py                                 |       11 |        0 |    100% |           |
| app/stuquiz/entities/category.py                               |        6 |        0 |    100% |           |
| app/stuquiz/entities/course.py                                 |       12 |        0 |    100% |           |
| app/stuquiz/entities/entity.py                                 |        3 |        0 |    100% |           |
| app/stuquiz/entities/question.py                               |       10 |        0 |    100% |           |
| app/stuquiz/entities/university.py                             |        6 |        0 |    100% |           |
| app/stuquiz/models/\_\_init\_\_.py                             |        0 |        0 |    100% |           |
| app/stuquiz/models/admin/\_\_init\_\_.py                       |        0 |        0 |    100% |           |
| app/stuquiz/models/admin/admin\_model.py                       |       36 |        7 |     81% |37, 44, 78-85 |
| app/stuquiz/repositories/\_\_init\_\_.py                       |        0 |        0 |    100% |           |
| app/stuquiz/repositories/abstract\_repository.py               |       37 |        7 |     81% |32-34, 46, 58, 70, 82 |
| app/stuquiz/repositories/admin\_repository.py                  |       16 |        0 |    100% |           |
| app/stuquiz/repositories/answer\_repository.py                 |       16 |        0 |    100% |           |
| app/stuquiz/repositories/category\_repository.py               |       16 |        0 |    100% |           |
| app/stuquiz/repositories/course\_repository.py                 |       16 |        0 |    100% |           |
| app/stuquiz/repositories/question\_repository.py               |       16 |        0 |    100% |           |
| app/stuquiz/repositories/university\_repository.py             |       16 |        0 |    100% |           |
| app/stuquiz/routes/\_\_init\_\_.py                             |        0 |        0 |    100% |           |
| app/stuquiz/routes/admin/\_\_init\_\_.py                       |        0 |        0 |    100% |           |
| app/stuquiz/routes/admin/login\_admin.py                       |        9 |        4 |     56% |     13-17 |
| app/stuquiz/routes/admin/logout\_admin.py                      |        6 |        1 |     83% |        13 |
| app/stuquiz/routes/router.py                                   |        5 |        2 |     60% |     12-13 |
| app/stuquiz/utils/\_\_init\_\_.py                              |        0 |        0 |    100% |           |
| app/stuquiz/utils/database\_provider.py                        |       14 |        7 |     50% |17-25, 30-32 |
| app/tests/\_\_init\_\_.py                                      |        0 |        0 |    100% |           |
| app/tests/controllers/\_\_init\_\_.py                          |        0 |        0 |    100% |           |
| app/tests/controllers/admin/\_\_init\_\_.py                    |        0 |        0 |    100% |           |
| app/tests/controllers/admin/test\_login\_admin\_controller.py  |       44 |        0 |    100% |           |
| app/tests/controllers/admin/test\_logout\_admin\_controller.py |       25 |        0 |    100% |           |
| app/tests/entities/test\_admin.py                              |        9 |        0 |    100% |           |
| app/tests/entities/test\_entity.py                             |       12 |        0 |    100% |           |
| app/tests/models/\_\_init\_\_.py                               |        0 |        0 |    100% |           |
| app/tests/models/admin/\_\_init\_\_.py                         |        0 |        0 |    100% |           |
| app/tests/models/admin/test\_admin\_model.py                   |       43 |        0 |    100% |           |
| app/tests/repositories/\_\_init\_\_.py                         |        0 |        0 |    100% |           |
| app/tests/repositories/test\_abstract\_repository.py           |       29 |        0 |    100% |           |
| app/tests/repositories/test\_admin\_repository.py              |       65 |        0 |    100% |           |
| app/tests/repositories/test\_answer\_repository.py             |       52 |        0 |    100% |           |
| app/tests/repositories/test\_category\_repository.py           |       51 |        0 |    100% |           |
| app/tests/repositories/test\_course\_repository.py             |       55 |        0 |    100% |           |
| app/tests/repositories/test\_question\_repository.py           |       52 |        0 |    100% |           |
| app/tests/repositories/test\_university\_repository.py         |       51 |        0 |    100% |           |
|                                                      **TOTAL** |  **809** |   **46** | **94%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/en0mia/stuquiz-api/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/en0mia/stuquiz-api/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/en0mia/stuquiz-api/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/en0mia/stuquiz-api/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fen0mia%2Fstuquiz-api%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/en0mia/stuquiz-api/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.