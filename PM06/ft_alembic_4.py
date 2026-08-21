import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using  'import alchemy'")
print("Testing create_air: ", alchemy.create_air())

print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", alchemy.create_earth())

# import alchemyを使用して、alchemyモジュールにアクセスし、
# そのあとairを作成

# create_earth()はモジュールインターフェースを通して公開されず、呼び出されると例外を発生させる
# 意図的にmypyエラーが発生する
