# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

%pip install wordcloud

import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Wörter, die in die Wordcloud aufgenommen werden sollen
words = "Fun Gamescom Power BI Fabric Australia"

# Erstellen der Wordcloud mit Farben im Blauton
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="Blues").generate(words)

# Anzeigen der Wordcloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
