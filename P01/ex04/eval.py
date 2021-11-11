
def check_value(coefs, words):
    if not isinstance(words, list) or not isinstance(coefs, list):
        raise ValueError("Need to pass 2 lists in args")
    if not (all(isinstance(word, str) for word in words)):
        raise ValueError("Words needs to have str only")
    if not (all(isinstance(coef, (float, int)) for coef in coefs)):
        raise ValueError("Coefs needs to have numbers only only")

class Evaluator():

    @staticmethod
    def zip_evaluate(coefs, words):
        check_value(coefs, words)
        if len(coefs) != len(words):
            return -1
        result = zip(coefs, words)
        count = sum((obj[0] * len(obj[1])) for obj in result)
        return count
           
    @staticmethod
    def enumerate_evaluate(coefs, words):
        check_value(coefs, words)
        if len(coefs) != len(words):
            return -1
        count = sum((coefs[key] * len(value)) for key,value in enumerate(words))
        return count

        