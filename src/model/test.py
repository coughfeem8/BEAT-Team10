import r2connection


r2 = r2connection.open("../server.out")

print(r2._cmd_process("aaa"))
print("All..........................................")
print(r2.cmdj("izzj"))