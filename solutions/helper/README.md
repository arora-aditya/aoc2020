# Helper methods

## `generateREADME`

Generates a nicely formatted with the name of the day's problems, and ranks for each of the parts
To generate, run the following from repository root:

```sh
make README
```

## `getInput`

Gets the input for a particular day and stores it in `day{xx}/` (assumes that directory exists)

Before you run this you will also have to create a `.env` file formatted the same as the `.sample.env`.
You can get your cookie by looking at the network requests on [https://adventofcode.com](https://adventofcode.com) after logging in and it would like the following:

![Cookie](https://i.imgur.com/vW92H3v.png)

**You should just save the part after `session=` in the `.env`**

Once you have set that up, you can get the input by running the following from repository root:

```sh
make day=<day_number>
```