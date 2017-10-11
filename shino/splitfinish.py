def chooseBestFeatureToSplit(dataSet):
    """chooseBestFeatureToSplit(ѡ����õ�����)

    Args:
        dataSet ���ݼ�
    Returns:
        bestFeature ���ŵ�������
    """
    # ���һ���ж����е� Feature, ���һ����label����
    numFeatures = len(dataSet[0]) - 1
    # ���ݼ���ԭʼ��Ϣ��
    baseEntropy = calcShannonEnt(dataSet)
    # ���ŵ���Ϣ����ֵ, �����ŵ�Featurn���
    bestInfoGain, bestFeature = 0.0, -1
    # iterate over all the features
    for i in range(numFeatures):
        # create a list of all the examples of this feature
        # ��ȡ��Ӧ��feature�µ���������
        featList = [example[i] for example in dataSet]
        # get a set of unique values
        # ��ȡ���غ�ļ��ϣ�ʹ��set��list���ݽ���ȥ��
        uniqueVals = set(featList)
        # ����һ����ʱ����Ϣ��
        newEntropy = 0.0
        # ����ĳһ�е�value���ϣ�������е���Ϣ�� 
        # ������ǰ�����е�����Ψһ����ֵ����ÿ��Ψһ����ֵ����һ�����ݼ����������ݼ�������ֵ����������Ψһ����ֵ�õ�������͡�
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            # �������
            prob = len(subDataSet)/float(len(dataSet))
            # ������Ϣ��
            newEntropy += prob * calcShannonEnt(subDataSet)
        # gain[��Ϣ����]: �������ݼ�ǰ�����Ϣ�仯�� ��ȡ��Ϣ������ֵ
        # ��Ϣ�������صļ��ٻ�������������ȵļ��١���󣬱Ƚ����������е���Ϣ���棬��������������ֵ�����ֵ��
        infoGain = baseEntropy - newEntropy
        print 'infoGain=', infoGain, 'bestFeature=', i, baseEntropy, newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
	def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # ������ݼ������һ�еĵ�һ��ֵ���ֵĴ���=�������ϵ�������Ҳ��˵ֻ��һ����𣬾�ֱֻ�ӷ��ؽ������
    # ��һ��ֹͣ���������е����ǩ��ȫ��ͬ����ֱ�ӷ��ظ����ǩ��
    # count() ������ͳ�������е�ֵ��list�г��ֵĴ���
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # ������ݼ�ֻ��1�У���ô�������label��������һ�࣬��Ϊ���
    # �ڶ���ֹͣ������ʹ������������������Ȼ���ܽ����ݼ����ֳɽ�����Ψһ���ķ��顣
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # ѡ�����ŵ��У��õ������ж�Ӧ��label����
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # ��ȡlabel������
    bestFeatLabel = labels[bestFeat]
    # ��ʼ��myTree
    myTree = {bestFeatLabel: {}}
    # ע��labels�б��ǿɱ������PYTHON��������Ϊ����ʱ��ַ���ã��ܹ���ȫ���޸�
    # �������д��뵼�º������ͬ��������ɾ����Ԫ�أ���������޷�ִ�У���ʾ'no surfacing' is not in list
    del(labels[bestFeat])
    # ȡ�������У�Ȼ������branch������
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        # ���ʣ��ı�ǩlabel
        subLabels = labels[:]
        # ������ǰѡ��������������������ֵ����ÿ�����ݼ������ϵݹ���ú���createTree()
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
        # print 'myTree', value, myTree
    return myTree
	def classify(inputTree, featLabels, testVec):
    """classify(������Ľڵ㣬���з���)

    Args:
        inputTree  ������ģ��
        featLabels Feature��ǩ��Ӧ������
        testVec    �������������
    Returns:
        classLabel ����Ľ��ֵ����Ҫӳ��label����֪������
    """
    # ��ȡtree�ĸ��ڵ���ڵ�keyֵ
    firstStr = inputTree.keys()[0]
    # ͨ��key�õ����ڵ��Ӧ��value
    secondDict = inputTree[firstStr]
    # �жϸ��ڵ����ƻ�ȡ���ڵ���label�е��Ⱥ�˳��������֪�������testVec��ô��ʼ��������������
    featIndex = featLabels.index(firstStr)
    # �������ݣ��ҵ����ڵ��Ӧ��labelλ�ã�Ҳ��֪������������ݵĵڼ�λ����ʼ����
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    print '+++', firstStr, 'xxx', secondDict, '---', key, '>>>', valueOfFeat
    # �жϷ�֦�Ƿ����: �ж�valueOfFeat�Ƿ���dict����
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel