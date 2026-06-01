# CSharp Log Priority Practice

## Description
A C# console practice project for custom queue/stack classes and a simple priority-sorted log.

## Original Context
This was an older learning project.

## How to Run
Run from the project folder:

```sh
dotnet run --project ConsoleApp1/ConsoleApp1.csproj
```

## Status
Partially works

## Cleanup Notes
- Renamed folder from `C# test` to `csharp-log-priority-practice`.
- Moved generated `bin/`, `obj/`, and editor settings into `_excluded_review/`.
- Fixed duplicate `Queue<T>` class by making `Stack.cs` define `Stack<T>`.
- Fixed `Queue<T>.Pop()` to return the removed item.
- Added small null fallbacks for console input.
- Added `.gitignore`.
