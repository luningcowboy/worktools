let tiny = require("tinify");
let child_process = require('child_process');
let keys = [
    "9nphs1dQaoxQOBf70uyeNH3v7kdbXNh0",
];
let to_path = 'res-new';
tiny.key = keys[0];

function tinyFile(file_name){
    let file = tiny.fromFile(file_name);
    file.toFile(file_name);
}
let json_files = [];
child_process.exec(`find ./res -name "*.png" `,(err, stdout, stderr)=>{
    if(err) console.log('copy exec error ==> ', err);
    else{
        json_files = stdout.split('\n');
        console.log(json_files.length);
        json_files.forEach(file_path=>{
            if(file_path && file_path !== ''){
                tinyFile(file_path);
            }
        })
    }
});

