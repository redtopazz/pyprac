import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

class HTMLTableParser:
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        return [(self.parse_html_table(table)) for table in soup.find_all('table')]

    def parse_html_table(self, table):
        n_columns = 0
        n_rows = 0
        column_names = []

        for row in table.find_all('tr'):
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows += 1
                if n_columns == 0:
                    n_columns = len(td_tags)
            th_tags = row.find_all('th')
            if len(th_tags) > 0 and len(column_names) == 0:
                for th in th_tags:
                    column_names.append(th.get_text())

        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column titles do not match the number of columns")

        #make df
        columns = column_names if len(column_names) > 0 else range(0, n_columns)
        df = pd.DataFrame(columns = columns, index = range(0, n_rows))
        row_marker = 0

        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                df.iat[row_marker, column_marker] = column.get_text()
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1

        for col in df:
            try:
                if col=='Rank':
                    continue
                df[col] = df[col].astype(float)
            except ValueError:
                pass
        return df

if __name__ == '__main__':
    url = "https://www.fantasypros.com/nfl/reports/leaders/rb.php?year=2015"

    hp = HTMLTableParser()
    table = hp.parse_url(url)[0]
    #print(table.head())

    fig, ax = plt.subplots()

    # Example data
    people = list(table['Player'][:10])
    y_pos = np.arange(len(people))
    performance = list(table['Avg'][:10])

    ax.barh(y_pos, performance, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Avg')
    ax.set_title('Top Running Bag\'s AVG')

    plt.show()
