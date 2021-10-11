const chalk = require('chalk');
const figlet = require('figlet');
const { Command } = require('commander');
const packageJson = require('./package.json');

// init a logo
console.log(chalk.yellow(figlet.textSync('zjt-cli', {
  horizontalLayout: 'full'
})));

const program = new Command();

// version
program
  .version(packageJson.version)
  .usage('<command [options]>');


// optional parameters
program.option('-c, --create', 'create a app project');


// create
program
  .command('create <app-name>')
  .description('create a new project')
  .option('-f, --force', 'overwrite target directory if it exists')
  .action(appname => {
    console.log(appname);
  });

program.on('-h, --help', () => {
  console.log();
  console.log('create by ataola, zjt-cli is a automation tool');
  console.log('about more, please visit https://zhengjiangtao.cn');
  console.log();
});

program.commands.forEach(command => command.on('--help', () => console.log()));

// parse arguments
program.parse(process.argv);

if (!process.argv.slice(2).length) {
  program.outputHelp();
}
