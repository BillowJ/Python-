function deleteBtn(url) {
    $.confirm({
        title: '提示',
        content: '是否删除?',
        buttons: {
            ok: {
                text: '确认',
                btnClass: 'btn-danger',
                action: function() {
                    location.href = url; //指向下载资源（此处为目标文件的输出数据流）
                }
            },
            cancel: {
                text: '取消',
                btnClass: 'btn-primary'
            }
        }
    });
}


function addBtn() {
    $.confirm({
        title: '提示',
        content: '是否添加?',
        buttons: {
            ok: {
                text: '确认',
                btnClass: 'btn-danger',
            },
            cancel: {
                text: '取消',
                btnClass: 'btn-primary'
            }
        }
    });
}
