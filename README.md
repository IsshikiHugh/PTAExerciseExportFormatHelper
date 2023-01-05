# PTA Exercises Export Format Helper

不想复习 FDS 的产物，当你拿到一张别人给你的导出试卷却发现全是选项不好做题怎么办？

遮住选项！但是太不方便了，虽然我尝试过用 Snipaste 来贴白纸，但是还是容易剧透。

恰好 PTA 的导出是 html 文件，于是就有了这个。

我比较懒，只删掉了影响做题的部分，有好心人可以做一下信息脱敏，像我这种做题拉跨怪都不好意思分享自己的低分卷呜呜呜。

## Usage

如你所见，`requirements.txt` 里只有一个 `bs4`。

然后使用：

```shell
python format.py <.../xxx.html>
```

就会在目标文件同级产生一个 `.../xxx_clean.html`，刚好我删掉了 `disabled` 属性，就可以互动式做题了（答案还是自己对x）。

其实把答案折叠起来更方便，但是我不会也暂时懒得学（？）。