# snowflakeazurestreamlit
CI/CD pipeline for deploying Streamlit apps to Snowflake stage

Note:

- This won't delete stages
- This won't delete Streamlit apps


Add these to your secrets

```

  SNOWSQL_ACCOUNT: ${{ secrets.ACCOUNT_REGION_PLATFORM }}
  SNOWSQL_USER:  ${{ secrets.SNOWFLAKE_USERNAME }}
  SNOWSQL_PWD: ${{ secrets.SNOWFLAKE_PASSWORD }}
  SNOWSQL_ROLE: ${{ secrets.SNOWFLAKE_ROLE }}


``` 
