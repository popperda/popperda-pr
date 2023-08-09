import flair 
import pandas as pd

sentimentmodel = flair.models.TextClassifier.load('en-sentiment')