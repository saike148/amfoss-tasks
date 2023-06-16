#### Server modifications

1. The port number in the localEndPoint variable was changed from `11000` to `8080`. 
2. The socket creation and declaration were changed to use the `using` statement
```using Socket listener = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);```
3. `int` datatype was added to the `bytesRec` variable.
4. Splitting of the received data was modified to split the string using a pipe character (`|`) in the line
```string[] dataArr = data.Split('|');```
5. A separator line was added for better visibility
```Console.WriteLine("====================================");```
6. File writing logic check was added:
```if (File.Exists(fileName))```

#### Client modifications

1. The socket creation and declaration were changed to use the `using` statement.
`using Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);`
2. Variables `name`, `intrests`, and `mail` were updated to specify datatypes as `string`.
3. Demlimiter was changed to use a pipe character (`|`).
```
string data = $"{name}|{intrests}|{mail}";
byte[] msg = Encoding.ASCII.GetBytes(data);
```
4. Socket was closed with `sender.Close();`

#### Working:
