from eval import Evaluator

try:
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    result = Evaluator.zip_evaluate(coefs, words)
    print(result)
    result2 = Evaluator.enumerate_evaluate(coefs, words)
    print(result2)

    words2 = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    result = Evaluator.zip_evaluate(coefs2, words2)
    print(result)
    result2 = Evaluator.enumerate_evaluate(coefs2, words2)
    print(result2)

except ValueError as err:
    print(err.args)