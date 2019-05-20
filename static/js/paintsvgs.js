
function getStylesheet(sheets, transformTable) {
    const iterArr = [].slice.call(sheets)
    const [styleSheetList] = iterArr.filter(
        x => x.href.includes(transformTable.stylePrefix)
    );
    const result = [].slice.call(styleSheetList.cssRules).reduce(
        (acc, x) => ({
            ...acc,
            [x.selectorText]: x
        }), {}
    );
    return result;
};

function paintMarkers(root, element, targetStyle, cssAttr) {
    const markers = [
        element.style["marker-start"],
        element.style["marker-end"],
    ].filter(x => x).map(x => x.match(/url\("(.*)"\)/)[1]);
    
    markers.map(
        m => {
            const path = root.querySelector(`${m} path`);
            path.style.stroke = targetStyle.style[cssAttr];
            path.style.fill = targetStyle.style[cssAttr];
        }
    );
};

function paintElement(pictureEntry, sheet, root, element) {
    function forMap(element) {
        // search pictureEntry by source class
        const [transformRecord] = pictureEntry.toPaint.filter(x => element.classList.contains(x.sourceClass));
        // loop nameMatches, select css class and apply svgAttr <- cssAttr
        transformRecord.nameMatches.map(match => {
            const [svgAttr, cssAttr, cssClass] = match;
            const selectorText = ['', ...cssClass.split(' ')].join('.');
            const targetStyle = sheet[selectorText];
            element.style[svgAttr] = targetStyle.style[cssAttr];
            paintMarkers(root, element, targetStyle, cssAttr);
        })
    };
    return forMap;
};

function paintPicture(pictures, transformTable, sheet) {
    const [head, ...tail] = pictures;
    if (!head) {
        return
    };
    const candidates = [].slice.call(
        head.contentDocument.querySelectorAll("[class]")
    );
    const pAlias = transformTable.picturesToProcess;
    const sameAs = pAlias[head.id].sameAs;
    candidates.map(
        paintElement(!sameAs ? pAlias[head.id] : pAlias[sameAs], sheet, head.contentDocument)
    );
    paintPicture(tail, transformTable, sheet);
};
