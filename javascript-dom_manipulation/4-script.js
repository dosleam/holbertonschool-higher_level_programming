document.getElementById('add_item').addEventListener('click', function () {
    const list = document.getElementsByClassName('my_list')[0];
    const item = document.createElement('li');

    item.innerHTML = 'Item';
    list.appendChild(item);
  });
