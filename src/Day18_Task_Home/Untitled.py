{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9ab81891-57cd-41a9-94fb-dfcbb816b937",
   "metadata": {},
   "outputs": [
    {
     "ename": "DatabaseError",
     "evalue": "Execution failed on sql '\nSELECT *\nFROM interns\nWHERE track = 'Data Science' AND stipend > 5000\n': no such table: interns",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mOperationalError\u001b[39m                          Traceback (most recent call last)",
      "\u001b[36mFile \u001b[39m\u001b[32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\sql.py:2664\u001b[39m, in \u001b[36mSQLiteDatabase.execute\u001b[39m\u001b[34m(self, sql, params)\u001b[39m\n\u001b[32m   2663\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m2664\u001b[39m     \u001b[43mcur\u001b[49m\u001b[43m.\u001b[49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43msql\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2665\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m cur\n",
      "\u001b[31mOperationalError\u001b[39m: no such table: interns",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[31mDatabaseError\u001b[39m                             Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[12]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      5\u001b[39m conn = sqlite3.connect(\u001b[33m\"\u001b[39m\u001b[33minternship.db\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      7\u001b[39m \u001b[38;5;66;03m# 1️⃣ Filter\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m df_filter = \u001b[43mpd\u001b[49m\u001b[43m.\u001b[49m\u001b[43mread_sql_query\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\"\"\u001b[39;49m\n\u001b[32m      9\u001b[39m \u001b[33;43mSELECT *\u001b[39;49m\n\u001b[32m     10\u001b[39m \u001b[33;43mFROM interns\u001b[39;49m\n\u001b[32m     11\u001b[39m \u001b[33;43mWHERE track = \u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mData Science\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[33;43m AND stipend > 5000\u001b[39;49m\n\u001b[32m     12\u001b[39m \u001b[33;43m\"\"\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconn\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m     14\u001b[39m \u001b[38;5;66;03m# 2️⃣ Average stipend\u001b[39;00m\n\u001b[32m     15\u001b[39m df_avg = pd.read_sql_query(\u001b[33m\"\"\"\u001b[39m\n\u001b[32m     16\u001b[39m \u001b[33mSELECT track, AVG(stipend) AS avg_stipend\u001b[39m\n\u001b[32m     17\u001b[39m \u001b[33mFROM interns\u001b[39m\n\u001b[32m     18\u001b[39m \u001b[33mGROUP BY track\u001b[39m\n\u001b[32m     19\u001b[39m \u001b[33m\"\"\"\u001b[39m, conn)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\sql.py:528\u001b[39m, in \u001b[36mread_sql_query\u001b[39m\u001b[34m(sql, con, index_col, coerce_float, params, parse_dates, chunksize, dtype, dtype_backend)\u001b[39m\n\u001b[32m    525\u001b[39m \u001b[38;5;28;01massert\u001b[39;00m dtype_backend \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m lib.no_default\n\u001b[32m    527\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m pandasSQL_builder(con) \u001b[38;5;28;01mas\u001b[39;00m pandas_sql:\n\u001b[32m--> \u001b[39m\u001b[32m528\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mpandas_sql\u001b[49m\u001b[43m.\u001b[49m\u001b[43mread_query\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    529\u001b[39m \u001b[43m        \u001b[49m\u001b[43msql\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    530\u001b[39m \u001b[43m        \u001b[49m\u001b[43mindex_col\u001b[49m\u001b[43m=\u001b[49m\u001b[43mindex_col\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    531\u001b[39m \u001b[43m        \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m=\u001b[49m\u001b[43mparams\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    532\u001b[39m \u001b[43m        \u001b[49m\u001b[43mcoerce_float\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcoerce_float\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    533\u001b[39m \u001b[43m        \u001b[49m\u001b[43mparse_dates\u001b[49m\u001b[43m=\u001b[49m\u001b[43mparse_dates\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    534\u001b[39m \u001b[43m        \u001b[49m\u001b[43mchunksize\u001b[49m\u001b[43m=\u001b[49m\u001b[43mchunksize\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    535\u001b[39m \u001b[43m        \u001b[49m\u001b[43mdtype\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdtype\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    536\u001b[39m \u001b[43m        \u001b[49m\u001b[43mdtype_backend\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdtype_backend\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    537\u001b[39m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\sql.py:2728\u001b[39m, in \u001b[36mSQLiteDatabase.read_query\u001b[39m\u001b[34m(self, sql, index_col, coerce_float, parse_dates, params, chunksize, dtype, dtype_backend)\u001b[39m\n\u001b[32m   2717\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mread_query\u001b[39m(\n\u001b[32m   2718\u001b[39m     \u001b[38;5;28mself\u001b[39m,\n\u001b[32m   2719\u001b[39m     sql,\n\u001b[32m   (...)\u001b[39m\u001b[32m   2726\u001b[39m     dtype_backend: DtypeBackend | Literal[\u001b[33m\"\u001b[39m\u001b[33mnumpy\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[33m\"\u001b[39m\u001b[33mnumpy\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   2727\u001b[39m ) -> DataFrame | Iterator[DataFrame]:\n\u001b[32m-> \u001b[39m\u001b[32m2728\u001b[39m     cursor = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43msql\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2729\u001b[39m     columns = [col_desc[\u001b[32m0\u001b[39m] \u001b[38;5;28;01mfor\u001b[39;00m col_desc \u001b[38;5;129;01min\u001b[39;00m cursor.description]\n\u001b[32m   2731\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[36mFile \u001b[39m\u001b[32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\sql.py:2676\u001b[39m, in \u001b[36mSQLiteDatabase.execute\u001b[39m\u001b[34m(self, sql, params)\u001b[39m\n\u001b[32m   2673\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m ex \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01minner_exc\u001b[39;00m\n\u001b[32m   2675\u001b[39m ex = DatabaseError(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mExecution failed on sql \u001b[39m\u001b[33m'\u001b[39m\u001b[38;5;132;01m{\u001b[39;00msql\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m'\u001b[39m\u001b[33m: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mexc\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m\"\u001b[39m)\n\u001b[32m-> \u001b[39m\u001b[32m2676\u001b[39m \u001b[38;5;28;01mraise\u001b[39;00m ex \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mexc\u001b[39;00m\n",
      "\u001b[31mDatabaseError\u001b[39m: Execution failed on sql '\nSELECT *\nFROM interns\nWHERE track = 'Data Science' AND stipend > 5000\n': no such table: interns"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "# Connect to database\n",
    "conn = sqlite3.connect(\"internship.db\")\n",
    "\n",
    "# 1️⃣ Filter\n",
    "df_filter = pd.read_sql_query(\"\"\"\n",
    "SELECT *\n",
    "FROM interns\n",
    "WHERE track = 'Data Science' AND stipend > 5000\n",
    "\"\"\", conn)\n",
    "\n",
    "# 2️⃣ Average stipend\n",
    "df_avg = pd.read_sql_query(\"\"\"\n",
    "SELECT track, AVG(stipend) AS avg_stipend\n",
    "FROM interns\n",
    "GROUP BY track\n",
    "\"\"\", conn)\n",
    "\n",
    "# 3️⃣ Count interns\n",
    "df_count = pd.read_sql_query(\"\"\"\n",
    "SELECT track, COUNT(*) AS total_interns\n",
    "FROM interns\n",
    "GROUP BY track\n",
    "\"\"\", conn)\n",
    "\n",
    "\n",
    "conn.close()\n",
    "df_filter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0049ab73-53e5-4243-8054-b197607ffa84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d763a4a7-5a6b-48a7-b800-18f98fa5afe7",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (1352991493.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[10]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mimport sqlite3\u001b[39m\n    ^\n\u001b[31mIndentationError\u001b[39m\u001b[31m:\u001b[39m unexpected indent\n"
     ]
    }
   ],
   "source": [
    " import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "# Connect to database\n",
    "conn = sqlite3.connect(\"internship.db\")\n",
    "\n",
    "# 1️⃣ Filter\n",
    "df_filter = pd.read_sql_query(\"\"\"\n",
    "SELECT *\n",
    "FROM interns\n",
    "WHERE track = 'Data Science' AND stipend > 5000\n",
    "\"\"\", conn)\n",
    "\n",
    "# 2️⃣ Average stipend\n",
    "df_avg = pd.read_sql_query(\"\"\"\n",
    "SELECT track, AVG(stipend) AS avg_stipend\n",
    "FROM interns\n",
    "GROUP BY track\n",
    "\"\"\", conn)\n",
    "\n",
    "# 3️⃣ Count interns\n",
    "df_count = pd.read_sql_query(\"\"\"\n",
    "SELECT track, COUNT(*) AS total_interns\n",
    "FROM interns\n",
    "GROUP BY track\n",
    "\"\"\", conn)\n",
    "\n",
    "conn.close()\n",
    "df_avg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4912769a-cf51-4bc7-ac6e-38efbcbc6493",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_count' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[43mdf_count\u001b[49m\n",
      "\u001b[31mNameError\u001b[39m: name 'df_count' is not defined"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "# Connect to database\n",
    "conn = sqlite3.connect(\"internship.db\")\n",
    "\n",
    "# 1️⃣ Filter\n",
    "df_filter = pd.read_sql_query(\"\"\"\n",
    "SELECT *\n",
    "FROM interns\n",
    "WHERE track = 'Data Science' AND stipend > 5000\n",
    "\"\"\", conn)\n",
    "\n",
    "# 2️⃣ Average stipend\n",
    "df_avg = pd.read_sql_query(\"\"\"\n",
    "SELECT track, AVG(stipend) AS avg_stipend\n",
    "FROM interns\n",
    "GROUP BY track\n",
    "\"\"\", conn)\n",
    "\n",
    "# 3️⃣ Count interns\n",
    "df_count = pd.read_sql_query(\"\"\"\n",
    "SELECT track, COUNT(*) AS total_interns\n",
    "FROM interns\n",
    "GROUP BY track\n",
    "\"\"\", conn)\n",
    "\n",
    "conn.close()\n",
    "df_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9012e32-84c1-478c-ade4-c32eabe287e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
