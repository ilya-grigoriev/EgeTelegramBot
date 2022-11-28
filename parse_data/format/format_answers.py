def format_answers_options(answers: list[str]) -> list[str]:
    formatted_answers = []
    for count, answer in enumerate(answers, start=1):
        formatted_answers.append(f'{count}) {answer}')
    return formatted_answers
