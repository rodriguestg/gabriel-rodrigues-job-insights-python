from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_keys = ['title', 'salary', 'type']
    dict_english = []
    for report in read_brazilian_file(path="tests/mocks/brazilians_jobs.csv"):
        for key in dict_keys:
            if key in report:
                dict_english.append(report)

    assert dict_english
