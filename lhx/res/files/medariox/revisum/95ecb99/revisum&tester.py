from tokenizer import LinesTokenizer
import tokenize
import io

hey = "with warnings.catch_warnings(): warnings.filterwarnings('ignore', category=UserWarning) clean_text = BeautifulSoup(clean_text, 'lxml').get_text()"

gu = LinesTokenizer(hey).tokens

for token in tokenize.generate_tokens(io.StringIO(hey).readline):
    print(token)

print(gu)
